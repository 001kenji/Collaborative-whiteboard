from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from typing import Dict, List, Optional
import uuid
import random
import asyncio
from datetime import datetime
import json, time

app = FastAPI(title="Collaborative Whiteboard API")

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://your-frontend.com",
        "http://localhost:3000"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ConnectionManager:
    def __init__(self):
        self.active_connections: Dict[str, Dict[str, WebSocket]] = {}
        self.board_data: Dict[str, Dict] = {}
        self.user_info: Dict[str, Dict[str, dict]] = {}  # board_id -> {user_id: user_data}
    
    async def accept_connection(self, websocket: WebSocket):
        await websocket.accept()
    
    async def register_user(self, websocket: WebSocket, board_id: str, user_data: dict):
        user_id = user_data.get('userId')
        user_name = user_data.get('userName')
        session_id = user_data.get('sessionId')
        
        # Generate new user if needed
        if not user_id:
            user_id = str(uuid.uuid4())
            session_id = str(uuid.uuid4())
            
            if not user_name:
                adjectives = ['Creative', 'Artistic', 'Clever', 'Bright', 'Quick', 'Witty', 'Sharp', 'Smart']
                nouns = ['Artist', 'Designer', 'Creator', 'Thinker', 'Drafter', 'Sketch', 'Drawer', 'Planner']
                user_name = f"{random.choice(adjectives)} {random.choice(nouns)}"
        
        # Initialize board if needed
        if board_id not in self.active_connections:
            self.active_connections[board_id] = {}
            self.board_data[board_id] = {
                "objects": [],  # Changed from elements to objects for Fabric.js
                "background": "#FFFFFF",
                "users": []
            }
            self.user_info[board_id] = {}
        
        # Assign color
        colors = ["#FF6B6B", "#4ECDC4", "#FFD166", "#06D6A0", "#118AB2", 
                  "#EF476F", "#7209B7", "#3A86FF", "#FB5607", "#8338EC"]
        used_colors = [u.get('color') for u in self.user_info[board_id].values()]
        available_colors = [c for c in colors if c not in used_colors]
        color = available_colors[0] if available_colors else colors[len(self.user_info[board_id]) % len(colors)]
        
        # Store user info
        self.user_info[board_id][user_id] = {
            "id": user_id,
            "name": user_name,
            "color": color,
            "session_id": session_id,
            "joined_at": datetime.now().isoformat(),
            "cursor": None
        }
        
        # Add to active connections
        self.active_connections[board_id][user_id] = websocket
        
        # Add to users list if not exists
        user_list_entry = {
            "id": user_id,
            "name": user_name,
            "color": color,
            "joined_at": datetime.now().isoformat()
        }
        
        existing_user = next((u for u in self.board_data[board_id]["users"] if u["id"] == user_id), None)
        if not existing_user:
            self.board_data[board_id]["users"].append(user_list_entry)
        
        return user_id, user_name, color, session_id
    
    def disconnect(self, board_id: str, user_id: str):
        if board_id in self.active_connections:
            if user_id in self.active_connections[board_id]:
                del self.active_connections[board_id][user_id]
            
            if board_id in self.user_info and user_id in self.user_info[board_id]:
                user_name = self.user_info[board_id][user_id]["name"]
                del self.user_info[board_id][user_id]
                
                # Remove from users list
                if board_id in self.board_data:
                    self.board_data[board_id]["users"] = [
                        u for u in self.board_data[board_id]["users"] if u["id"] != user_id
                    ]
                
                # Clean empty boards
                if not self.active_connections[board_id]:
                    del self.active_connections[board_id]
                    del self.board_data[board_id]
                    del self.user_info[board_id]
                
                return user_name
        return "User"
    
    async def broadcast(self, board_id: str, message: dict, exclude_user_id: str = None):
        if board_id in self.active_connections:
            disconnected = []
            for user_id, connection in self.active_connections[board_id].items():
                # Send to ALL users (remove exclude_user_id check temporarily for debugging)
                try:
                    await connection.send_json(message)
                    print(f"Sent {message['type']} to user {user_id}")
                except Exception as e:
                    print(f"Failed to send to user {user_id}: {e}")
                    disconnected.append(user_id)
            
            for user_id in disconnected:
                self.disconnect(board_id, user_id)

    async def send_to_user(self, websocket: WebSocket, message: dict):
        await websocket.send_json(message)
    
    async def add_object(self, board_id: str, obj_data: dict):
        if board_id in self.board_data:
            obj_data["id"] = str(uuid.uuid4())
            obj_data["timestamp"] = datetime.now().isoformat()
            self.board_data[board_id]["objects"].append(obj_data)
            
            # Limit objects to prevent memory issues
            if len(self.board_data[board_id]["objects"]) > 1000:
                self.board_data[board_id]["objects"] = self.board_data[board_id]["objects"][-1000:]

manager = ConnectionManager()

# In the WebSocket handler, fixed the object removal case
@app.websocket("/ws/{board_id}")
async def websocket_endpoint(websocket: WebSocket, board_id: str):
    user_id = None
    user_name = None
    boardId = None
    
    try:
        await manager.accept_connection(websocket)
        
        # First message must be user_join
        data = await websocket.receive_json()
        
        if data["type"] == "user_join":
            user_id, user_name, color, session_id = await manager.register_user(
                websocket, board_id, data
            )
            
            # Send initial data
            await manager.send_to_user(websocket, {
                    "type": "init",
                    "user_id": user_id,
                    "user_name": user_name,
                    "user_color": color,
                    "session_id": session_id,
                    "board_data": manager.board_data.get(board_id, {"objects": [], "users": [], "background": "#FFFFFF"}),
                    "users": manager.board_data.get(board_id, {}).get("users", [])
                })
            
            # Also send each existing object individually for reliability
            # if board_id in manager.board_data:
            #     for obj in manager.board_data[board_id]["objects"]:
            #         await manager.send_to_user(websocket, {
            #             "type": "object_added",
            #             "object": obj
            #         })
                            
            # Notify others
            await manager.broadcast(board_id, {
                "type": "user_joined",
                "user": {
                    "id": user_id,
                    "name": user_name,
                    "color": color,
                    "joined_at": datetime.now().isoformat()
                }
            }, exclude_user_id=user_id)
            
            # Handle subsequent messages
            try:
                while True:
                    data = await websocket.receive_json()
                    
                    if data["type"] == "add_object":
                        obj_data = data["object"]
                        
                        # Ensure object has required fields
                        if not obj_data.get("id"):
                            obj_data["id"] = f"obj_{int(datetime.now().timestamp() * 1000)}_{random.randint(1000, 9999)}"
                        
                        obj_data["timestamp"] = datetime.now().isoformat()
                        
                        # Store in board data
                        if board_id in manager.board_data:
                            manager.board_data[board_id]["objects"].append(obj_data)
                        
                        # Broadcast to all users
                        await manager.broadcast(board_id, {
                            "type": "object_added",
                            "object": obj_data
                        })
                    # In the WebSocket handler, add this case:
                    elif data["type"] == "update_user":
                        old_name = data.get("oldName")
                        new_name = data.get("newName")
                        user_id = data.get("userId")
                        
                        # Update user info
                        if (board_id in manager.user_info and 
                            user_id in manager.user_info[board_id]):
                            manager.user_info[board_id][user_id]["name"] = new_name
                        
                        # Update users list
                        if board_id in manager.board_data:
                            for user in manager.board_data[board_id]["users"]:
                                if user["id"] == user_id:
                                    user["name"] = new_name
                                    break
                        
                        # Broadcast the update to all users
                        await manager.broadcast(board_id, {
                            "type": "user_updated",
                            "user_id": user_id,
                            "oldName": old_name,
                            "newName": new_name
                        }, exclude_user_id=user_id)
                    
                    elif data["type"] == "modify_object":
                        obj_data = data["object"]
                        object_id = data.get('object_id') or obj_data.get('id')
                        
                        print(f"📝 Modify object request - ID: {object_id}")
                        
                        if board_id in manager.board_data:
                            # Find and replace the existing object
                            for i, obj in enumerate(manager.board_data[board_id]["objects"]):
                                if obj.get("id") == object_id:
                                    # Replace the entire object with new data
                                    manager.board_data[board_id]["objects"][i] = obj_data
                                    print(f'✅ Replaced object: {object_id}')
                                    break
                            else:
                                print(f'❌ Object not found in board data: {object_id}')
                        
                        # Ensure the object data has the correct ID
                        if 'id' not in obj_data and object_id:
                            obj_data['id'] = object_id
                        
                        # Broadcast the new object data
                        await manager.broadcast(board_id, {
                            "type": "object_modified",
                            "object": obj_data,
                            "object_id": object_id
                        })
                                        
                    elif data["type"] == "remove_object":
                        obj_id = data.get("object_id") or data.get("object", {}).get("id")
                        if obj_id and board_id in manager.board_data:
                            manager.board_data[board_id]["objects"] = [
                                obj for obj in manager.board_data[board_id]["objects"] 
                                if obj.get("id") != obj_id
                            ]
                        
                        await manager.broadcast(board_id, {
                            "type": "object_removed",
                            "object_id": obj_id
                        })
                    
                    elif data["type"] == "clear_board":
                        if board_id in manager.board_data:
                            manager.board_data[board_id]["objects"] = []
                        
                        await manager.broadcast(board_id, {
                            "type": "clear_board",
                            "user_id": data.get("user_id", user_id),
                            "user_name": data.get("user_name", user_name),
                            "boardId": data.get("boardId", boardId)
                        })
                    
                    elif data["type"] == "cursor_move":
                        if board_id in manager.user_info and user_id in manager.user_info[board_id]:
                            manager.user_info[board_id][user_id]["cursor"] = data["position"]
                        
                        user_info = manager.user_info.get(board_id, {}).get(user_id, {})
                        
                        await manager.broadcast(board_id, {
                            "type": "cursor_moved",
                            "user_id": user_id,
                            "user_name": user_info.get("name", "User"),
                            "user_color": user_info.get("color", "#999999"),
                            "position": data["position"]
                        }, exclude_user_id=user_id)
                    
                    elif data["type"] == "update_user":
                        old_name = data.get("oldName")
                        new_name = data.get("newName")
                        
                        # Update user info
                        if (board_id in manager.user_info and 
                            user_id in manager.user_info[board_id]):
                            manager.user_info[board_id][user_id]["name"] = new_name
                        
                        # Update users list
                        if board_id in manager.board_data:
                            for user in manager.board_data[board_id]["users"]:
                                if user["id"] == user_id:
                                    user["name"] = new_name
                                    break
                        
                        await manager.broadcast(board_id, {
                            "type": "user_updated",
                            "user_id": user_id,
                            "oldName": old_name,
                            "newName": new_name
                        }, exclude_user_id=user_id)
                    
                    elif data["type"] == "ping":
                        await manager.send_to_user(websocket, {"type": "pong"})
            
            except WebSocketDisconnect:
                pass
            
            finally:
                if user_id:
                    disconnected_name = manager.disconnect(board_id, user_id)
                    await manager.broadcast(board_id, {
                        "type": "user_left",
                        "user_id": user_id,
                        "user_name": disconnected_name or user_name
                    })
    
    except Exception as e:
        print(f"WebSocket error: {e}")
        try:
            await websocket.close()
        except:
            pass


@app.get("/")
async def root():
    return {"message": "Whiteboard API is running"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)