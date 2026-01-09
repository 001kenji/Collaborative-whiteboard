<template>
  <div class="fabric-whiteboard">
    <!-- Toolbar -->
    <div class="toolbar">
      <div class="toolbar-section">
        <button @click="selectTool('select')" :class="{ active: activeTool === 'select' }" title="Select">
          <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 8V4m0 0h4M4 4l5 5m11-1V4m0 0h-4m4 0l-5 5M4 16v4m0 0h4m-4 0l5-5m11 5v-4m0 4h-4m4 0l-5-5" />
          </svg>
        </button>
        <button @click="selectTool('pencil')" :class="{ active: activeTool === 'pencil' }" title="Pencil">
          <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15.232 5.232l3.536 3.536m-2.036-5.036a2.5 2.5 0 113.536 3.536L6.5 21.036H3v-3.572L16.732 3.732z" />
          </svg>
        </button>
        
        <button @click="selectTool('rectangle')" :class="{ active: activeTool === 'rectangle' }" title="Rectangle">
          <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h14a2 2 0 012 2v14a2 2 0 01-2 2H5a2 2 0 01-2-2V5z" />
          </svg>
        </button>
        <button @click="selectTool('circle')" :class="{ active: activeTool === 'circle' }" title="Circle">
          <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
          </svg>
        </button>
        <button @click="selectTool('text')" :class="{ active: activeTool === 'text' }" title="Text">
          <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 10h18M3 14h18m-9-4v8m-7 0h14a2 2 0 002-2V8a2 2 0 00-2-2H5a2 2 0 00-2 2v8a2 2 0 002 2z" />
          </svg>
        </button>
        <button @click="selectTool('eraser')" :class="{ active: activeTool === 'eraser' }" title="Eraser">
          <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16" />
          </svg>
        </button>
      </div>
      
      <div class="toolbar-section">
        <div class="color-picker">
          <button
            v-for="color in colors"
            :key="color"
            @click="setColor(color)"
            :class="{ active: strokeColor === color }"
            :style="{ backgroundColor: color }"
            :title="color"
          />
        </div>
        <input type="color" v-model="strokeColor" @input="setColor(strokeColor)" />
      </div>
      
      <div class="toolbar-section">
        <label>Size:</label>
        <input type="range" min="1" max="50" v-model="strokeWidth" @input="setStrokeWidth" />
        <span>{{ strokeWidth }}px</span>
      </div>
      
      <div class="toolbar-section">
        <button @click="toggleFill" :class="{ active: fillEnabled }" title="Fill">
          Fill
        </button>
        <input v-if="fillEnabled" type="color" v-model="fillColor" @input="setFillColor" />
      </div>
      
      <div class="toolbar-section">
        <button @click="undo" :disabled="!canUndo" title="Undo">
          <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 10h10a8 8 0 018 8v2M3 10l6 6m-6-6l6-6" />
          </svg>
        </button>
        <button @click="redo" :disabled="!canRedo" title="Redo">
          <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3" />
          </svg>
        </button>
        <button @click="clearCanvas" title="Clear">
          <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16" />
          </svg>
        </button>
      </div>
      
      <div class="toolbar-section">
        <button @click="toggleGrid" :class="{ active: showGrid }" title="Grid">
          Grid
        </button>
        <button @click="toggleSnap" :class="{ active: snapToGrid }" title="Snap to Grid">
          Snap
        </button>
        <button @click="zoomIn" title="Zoom In">+</button>
        <button @click="zoomOut" title="Zoom Out">-</button>
        <button @click="resetZoom" title="Reset Zoom">1:1</button>
        <span class="zoom-level">{{ Math.round(zoom * 100) }}%</span>
      </div>
      
      <div class="toolbar-section">
        <button @click="exportJSON" title="Export JSON">
          Export
        </button>
        <button @click="exportImage" title="Export Image">
          <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 0 00-2 2v12a2 2 0 002 2z" />
          </svg>
        </button>
        <button @click="importJSON" title="Import JSON">
          Import
        </button>
      </div>

      <div class="toolbar-section">
        <label class="right-click-toggle">
          <input type="checkbox" v-model="rightClickEnabled" />
          Right-click toggle
        </label>
      </div>
    </div>
    
    <!-- Canvas Container -->
    <div  class="canvas-container" ref="canvasContainer">
      <canvas  ref="canvas"></canvas>
      
      <!-- Live Cursors -->
      <div class="cursors-overlay">
        <div
          v-for="(cursor, userId) in liveCursors"
          :key="userId"
          class="cursor"
          :style="{
            left: cursor.x + 'px',
            top: cursor.y + 'px',
            borderColor: cursor.color
          }"
          :title="cursor.name"
        >
          <div class="cursor-dot" :style="{ backgroundColor: cursor.color }"></div>
          <div class="cursor-name">{{ cursor.name }}</div>
        </div>
      </div>
    </div>
    
    <!-- Text Input Modal -->
    <div v-if="textInputActive" class="text-input-modal">
      <div class="modal-content">
        <h3>Add Text</h3>
        <input
          v-model="textInput"
          @keyup.enter="addText"
          @keyup.esc="cancelText"
          placeholder="Enter text..."
          ref="textInputField"
          autofocus
        />
        <div class="modal-actions">
          <button @click="addText">Add</button>
          <button @click="cancelText">Cancel</button>
        </div>
      </div>
    </div>
    
    <!-- Name Change Button -->
    <div class="name-change-btn">
      <button @click="showNameChange = true" title="Change your name">
        {{ props.userName || 'User' }}
        <svg class="w-4 h-4 ml-1" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z" />
        </svg>
      </button>
    </div>

    <!-- Name Change Modal -->
    <div v-if="showNameChange" class="name-change-modal">
      <div class="modal-content">
        <h3>Change Your Name</h3>
        <input
          v-model="newUserName"
          @keyup.enter="updateUserName"
          placeholder="Enter new name"
          class="name-input"
          autofocus
        />
        <div class="modal-actions">
          <button @click="updateUserName" class="btn-primary">Update</button>
          <button @click="showNameChange = false" class="btn-secondary">Cancel</button>
        </div>
      </div>
    </div>
    
    <!-- Stickers Panel -->
    <div v-if="showStickers" class="stickers-panel">
      <h3>Stickers & Emojis</h3>
      <div class="stickers-grid">
        <button
          v-for="sticker in stickers"
          :key="sticker.emoji"
          @click="addSticker(sticker)"
          class="sticker-btn"
          :title="sticker.name"
        >
          {{ sticker.emoji }}
        </button>
      </div>
    </div>
    
    <!-- History Timeline -->
    <div v-if="showHistory" class="history-timeline">
      <h3>History</h3>
      <div class="history-list">
        <div
          v-for="(action, index) in history"
          :key="index"
          @click="restoreHistory(index)"
          :class="{ active: historyIndex === index }"
          class="history-item"
        >
          {{ action.type }} - {{ new Date(action.timestamp).toLocaleTimeString() }}
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted, watch, computed, nextTick } from 'vue'
import { push } from 'notivue'
import { fabric } from 'fabric'

const props = defineProps({
  boardId: String,
  userId: String,
  userName: String,
  userColor: String,
  socket: Object
})

const emit = defineEmits(['update-users', 'board-cleared', 'user-name-changed'])

const notificationStore = push

// Refs
const canvasContainer = ref(null)
const canvas = ref(null)
const textInputField = ref(null)
let fabricCanvas = null

// Drawing state
const isDrawing = ref(false)
const isRightClickMode = ref(false)
const rightClickEnabled = ref(true)

// State variables
const activeTool = ref('select')
const strokeColor = ref('#FF6B6B')
const fillColor = ref('#FF6B6B')
const strokeWidth = ref(5)
const fillEnabled = ref(false)
const showGrid = ref(false)
const snapToGrid = ref(false)
const zoom = ref(1)
const textInputActive = ref(false)
const textInput = ref('')
const textPosition = ref({ x: 0, y: 0 })
const showStickers = ref(false)
const showHistory = ref(false)
const history = ref([])
const historyIndex = ref(-1)
const liveCursors = ref({})
const showNameChange = ref(false)
const newUserName = ref('')
const lastCursorUpdate = ref(0)
const lastX = ref(0)
const lastY = ref(0)
// Constants
const colors = [
  '#FF6B6B', '#4ECDC4', '#FFD166', '#06D6A0',
  '#118AB2', '#EF476F', '#7209B7', '#3A86FF',
  '#FB5607', '#8338EC', '#000000', '#FFFFFF'
]

const stickers = [
  { emoji: '⭐', name: 'Star', type: 'star' },
  { emoji: '❤️', name: 'Heart', type: 'heart' },
  { emoji: '👍', name: 'Thumbs Up', type: 'thumbs-up' },
  { emoji: '😂', name: 'Laughing', type: 'laughing' },
  { emoji: '🔥', name: 'Fire', type: 'fire' },
  { emoji: '🚀', name: 'Rocket', type: 'rocket' },
  { emoji: '💡', name: 'Light Bulb', type: 'light-bulb' },
  { emoji: '📌', name: 'Pin', type: 'pin' },
  { emoji: '📍', name: 'Round Pin', type: 'round-pin' },
  { emoji: '💬', name: 'Speech Bubble', type: 'speech-bubble' }
]

const gridSize = 20

// Computed
const canUndo = computed(() => historyIndex.value > 0)
const canRedo = computed(() => historyIndex.value < history.value.length - 1)

// ========== MISSING FUNCTIONS DEFINED BELOW ==========

// Initialize Fabric.js Canvas
const initCanvas = () => {
  if (!canvasContainer.value) return
  
  const containerWidth = canvasContainer.value.clientWidth
  const containerHeight = canvasContainer.value.clientHeight
  
  fabricCanvas = new fabric.Canvas(canvas.value, {
    width: containerWidth,
    height: containerHeight,
    backgroundColor: '#ffffff',
    selection: true,
    selectionColor: 'rgba(100, 100, 255, 0.3)',
    selectionBorderColor: 'blue',
    selectionLineWidth: 2,
    preserveObjectStacking: true,
    stopContextMenu: true
  })
  
  // Setup event listeners
  setupCanvasEvents()
  
  // Setup grid
  if (showGrid.value) {
    drawGrid()
  }
  
  // Auto-save
  startAutoSave()
}

// History Management Functions
const saveToHistory = (type, object) => {
  const objectJSON = object.toObject()
  objectJSON['id'] = object.id
  objectJSON._historyId = Date.now()
  
  history.value = history.value.slice(0, historyIndex.value + 1)
  history.value.push({
    type,
    object: objectJSON,
    timestamp: new Date().toISOString()
  })
  
  historyIndex.value = history.value.length - 1
}

const undo = () => {
  if (!canUndo.value || !fabricCanvas) return
  
  historyIndex.value--
  restoreCanvasFromHistory()
}

const redo = () => {
  if (!canRedo.value || !fabricCanvas) return
  
  historyIndex.value++
  restoreCanvasFromHistory()
}

const restoreCanvasFromHistory = () => {
  if (!fabricCanvas) return
  
  fabricCanvas.clear()
  
  for (let i = 0; i <= historyIndex.value; i++) {
    const action = history.value[i]
    if (action.type !== 'remove') {
      fabric.util.enlivenObjects([action.object], (objects) => {
        objects.forEach(obj => {
          obj._remote = true
          fabricCanvas.add(obj)
        })
        fabricCanvas.renderAll()
      })
    }
  }
}

const restoreHistory = (index) => {
  historyIndex.value = index
  restoreCanvasFromHistory()
}

// Auto-save Function
const startAutoSave = () => {
  setInterval(() => {
    if (fabricCanvas && history.value.length > 0) {
      localStorage.setItem(`whiteboard_autosave_${props.boardId}`, JSON.stringify({
        canvas: fabricCanvas.toJSON(),
        history: history.value,
        historyIndex: historyIndex.value,
        timestamp: new Date().toISOString()
      }))
    }
  }, 30000)
}

const loadAutoSave = () => {
  const saved = localStorage.getItem(`whiteboard_autosave_${props.boardId}`)
  if (saved && fabricCanvas) {
    try {
      const data = JSON.parse(saved)
      fabricCanvas.loadFromJSON(data.canvas, () => {
        history.value = data.history || []
        historyIndex.value = data.historyIndex || -1
        fabricCanvas.renderAll()
        notificationStore.info('Auto-save Loaded', 'Restored from last session')
      })
    } catch (error) {
      console.error('Failed to load auto-save:', error)
    }
  }
}

// ========== CONTINUATION OF PREVIOUS FUNCTIONS ==========

const setupCanvasEvents = () => {
  if (!fabricCanvas) return
  
  // Clear all existing listeners
  fabricCanvas.off()

  // Setup cursor tracking FIRST
  setupCursorTracking()
  
  // Object added (including shapes)
  fabricCanvas.on('object:added', (e) => {
    if (e.target && !e.target._remote) {
      console.log('Object added locally:', e.target.type)
      saveToHistory('add', e.target)
      sendObjectToServer(e.target, 'add')
    }
  })
  
  // Object modified
  fabricCanvas.on('object:modified', (e) => {
    if (e.target && !e.target._remote) {
      console.log('Object modified locally:', e.target.type)
      saveToHistory('modify', e.target)
      sendObjectToServer(e.target, 'modify')
    }
  })
  
  // Text editing
  fabricCanvas.on('text:changed', (e) => {
    if (e.target && !e.target._remote) {
      console.log('Text changed locally')
      saveToHistory('modify', e.target)
      sendObjectToServer(e.target, 'modify')
    }
  })
  
  // Object removed
  fabricCanvas.on('object:removed', (e) => {
    if (e.target && !e.target._remote) {
      console.log('Object removed locally:', e.target.type)
      saveToHistory('remove', e.target)
      sendObjectToServer(e.target, 'remove')
    }
  })
  
  // Mouse move for cursor tracking
  
    // fabricCanvas.on('mouse:move', (e) => {
    //     console.log('🖱️ Mouse move detected')
    //     console.log('reached')
    //     if (!props.socket) {
    //         console.log('❌ No socket available')
    //         return
    //     }
        
    //     console.log('🖱️ WebSocket state:', props.socket.readyState, 'OPEN=', WebSocket.OPEN)
        
    //     if (props.socket.readyState === WebSocket.OPEN) {
    //         const pointer = fabricCanvas.getPointer(e.e)
    //         console.log('🖱️ Pointer position:', pointer.x, pointer.y)
            
    //         // Fix throttle logic
    //         const now = Date.now()
    //         const lastUpdate = lastCursorUpdate.value || 0
            
    //         if (now - lastUpdate > 50) { // Send every 50ms max
    //         console.log('🖱️ Sending cursor update')
            
    //         const cursorData = {
    //             type: 'cursor_move',
    //             position: { x: pointer.x, y: pointer.y },
    //             user_id: props.userId,
    //             user_name: props.userName,
    //             user_color: props.userColor
    //         }
            
    //         console.log('📤 Sending cursor data:', cursorData)
    //         props.socket.send(JSON.stringify(cursorData))
    //         lastCursorUpdate.value = now
    //         } else {
    //         console.log('🖱️ Throttled cursor update (too soon)')
    //         }
    //     } else {
    //         console.log('❌ WebSocket not open, state:', props.socket.readyState)
    //     }
    // })

    
  
  // Right-click handling
  fabricCanvas.on('mouse:down', (e) => {
    
    if (e.e.button === 2) {
      e.e.preventDefault()
      
      if (rightClickEnabled.value) {
        isRightClickMode.value = !isRightClickMode.value
        
        if (isRightClickMode.value) {
          fabricCanvas.selection = false
          fabricCanvas.defaultCursor = 'grab'
          notificationStore.info('Navigation Mode', 'Right-click again to draw')
        } else {
          fabricCanvas.selection = true
          fabricCanvas.defaultCursor = 'default'
          notificationStore.info('Drawing Mode', 'Right-click to navigate')
        }
      }
    }
  })
  
  // Text tool click
  // Text tool click handler
    fabricCanvas.on('mouse:down', (e) => {
        
    if (activeTool.value === 'text' && e.e.button === 0) {
        const pointer = fabricCanvas.getPointer(e.e)
        showTextInput(pointer.x, pointer.y)
    }
    })
  
  // Mouse wheel for zoom
  fabricCanvas.on('mouse:wheel', (e) => {
    
    e.e.preventDefault()
    const delta = e.e.deltaY
    const zoomFactor = 0.05
    
    if (delta > 0) {
      zoomOut()
    } else {
      zoomIn()
    }
  })
}



// Drawing Tools
const selectTool = (tool) => {
  activeTool.value = tool
  
  if (!fabricCanvas) return
  
  // IMPORTANT: Always disable drawing mode first
  fabricCanvas.isDrawingMode = false
  fabricCanvas.selection = true
  fabricCanvas.defaultCursor = 'default'
  fabricCanvas.skipTargetFind = false
  
  // Clean up ALL existing event listeners
  fabricCanvas.off('mouse:down')
  fabricCanvas.off('mouse:move')
  fabricCanvas.off('mouse:up')

   // Clean up container listeners for drawing tools
    if (canvasContainer.value && canvasContainer.value._drawingHandlers) {
        canvasContainer.value.removeEventListener('mousedown', canvasContainer.value._drawingHandlers.mousedown)
        canvasContainer.value.removeEventListener('mousemove', canvasContainer.value._drawingHandlers.mousemove)
        canvasContainer.value.removeEventListener('mouseup', canvasContainer.value._drawingHandlers.mouseup)
        delete canvasContainer.value._drawingHandlers
    }
  // Reset any drawing state
  isDrawing.value = false

    // Add container event listeners for drawing tools
  let containerMouseDownHandler, containerMouseMoveHandler, containerMouseUpHandler
  
  
  
  switch (tool) {
    case 'select':
      fabricCanvas.selection = true
      fabricCanvas.defaultCursor = 'default'
      break
      
    case 'pencil':
      fabricCanvas.isDrawingMode = true
      const pencilBrush = new fabric.PencilBrush(fabricCanvas)
      pencilBrush.color = strokeColor.value
      pencilBrush.width = strokeWidth.value
      fabricCanvas.freeDrawingBrush = pencilBrush
      fabricCanvas.defaultCursor = 'crosshair'
      break
      
    // case 'line':
    //   setupLineTool()
    //   break
      
    // case 'rectangle':
    //   setupRectangleTool()
    //   break
      
    // case 'circle':
    //   setupCircleTool()
    //   break
      
    // case 'text':
    //   fabricCanvas.defaultCursor = 'text'
    //   fabricCanvas.selection = false  // Disable selection for text tool
      
    //   // Setup text tool click handler
    //   setupTextTool()
    //   break

    case 'line':
    case 'rectangle':
    case 'circle':
      // These will use container events for better performance
      setupContainerDrawingTool(tool)
      break
      
    case 'eraser':
      setupEraserTool()
      break
  }
}

const setupContainerDrawingTool = (tool) => {
  if (!fabricCanvas || !canvasContainer.value) return
  
  fabricCanvas.selection = false
  fabricCanvas.defaultCursor = 'crosshair'
  
  let shape = null
  let startPoint = null
  let isDrawing = false
  
  const handleContainerMouseDown = (e) => {
    if (e.button !== 0 || isRightClickMode.value) return
    
    e.preventDefault()
    const rect = canvasContainer.value.getBoundingClientRect()
    const x = e.clientX - rect.left
    const y = e.clientY - rect.top
    
    // Adjust for zoom
    const adjustedX = x / zoom.value
    const adjustedY = y / zoom.value
    
    startPoint = { x: adjustedX, y: adjustedY }
    isDrawing = true
    
    // Create shape based on tool
    if (tool === 'rectangle') {
      shape = new fabric.Rect({
        left: adjustedX,
        top: adjustedY,
        width: 0,
        height: 0,
        stroke: strokeColor.value,
        strokeWidth: strokeWidth.value,
        fill: fillEnabled.value ? fillColor.value : 'transparent',
        strokeUniform: true,
        selectable: true,
        _remote: false,
        _isDrawing: true,
        id: `rect_${Date.now()}_${Math.random().toString(36).substr(2, 9)}`
      })
    } else if (tool === 'circle') {
      shape = new fabric.Circle({
        left: adjustedX,
        top: adjustedY,
        radius: 0,
        stroke: strokeColor.value,
        strokeWidth: strokeWidth.value,
        fill: fillEnabled.value ? fillColor.value : 'transparent',
        strokeUniform: true,
        selectable: true,
        _remote: false,
        _isDrawing: true,
        id: `circle_${Date.now()}_${Math.random().toString(36).substr(2, 9)}`
      })
    }
    
    if (shape) {
      fabricCanvas.add(shape)
      fabricCanvas.setActiveObject(shape)
    }
  }
  
  const handleContainerMouseMove = (e) => {
    if (!isDrawing || !shape) return
    
    e.preventDefault()
    const rect = canvasContainer.value.getBoundingClientRect()
    const x = e.clientX - rect.left
    const y = e.clientY - rect.top
    
    // Adjust for zoom
    const adjustedX = x / zoom.value
    const adjustedY = y / zoom.value
    
    if (tool === 'rectangle') {
      const width = adjustedX - startPoint.x
      const height = adjustedY - startPoint.y
      
      shape.set({
        width: Math.abs(width),
        height: Math.abs(height),
        left: width > 0 ? startPoint.x : adjustedX,
        top: height > 0 ? startPoint.y : adjustedY
      })
    } else if (tool === 'circle') {
      const radius = Math.sqrt(
        Math.pow(adjustedX - startPoint.x, 2) +
        Math.pow(adjustedY - startPoint.y, 2)
      )
      
      shape.set({
        radius: radius,
        left: startPoint.x - radius,
        top: startPoint.y - radius
      })
    }
    
    fabricCanvas.renderAll()
  }
  
  const handleContainerMouseUp = (e) => {
    if (!isDrawing || !shape) return
    
    isDrawing = false
    shape._isDrawing = false
    
    // Validate and send shape
    if (shape.radius >= 5 || (shape.width >= 5 && shape.height >= 5)) {
      console.log(`${tool} completed, sending to server:`)
      saveToHistory('add', shape)
      sendObjectToServer(shape, 'add')
    } else {
      fabricCanvas.remove(shape)
      notificationStore.info('Shape too small', 'Please draw a larger shape')
    }
    
    shape = null
    startPoint = null
    
    // Auto-switch back to select tool
    setTimeout(() => {
      if (activeTool.value === tool) {
        selectTool('select')
      }
    }, 50)
  }
  
  // Add event listeners to container
  canvasContainer.value.addEventListener('mousedown', handleContainerMouseDown)
  canvasContainer.value.addEventListener('mousemove', handleContainerMouseMove)
  canvasContainer.value.addEventListener('mouseup', handleContainerMouseUp)
  
  // Store handlers for cleanup
  canvasContainer.value._drawingHandlers = {
    mousedown: handleContainerMouseDown,
    mousemove: handleContainerMouseMove,
    mouseup: handleContainerMouseUp
  }
}

const setupTextTool = () => {
  if (!fabricCanvas) return
  
  // Clear any existing mouse down handlers
  fabricCanvas.off('mouse:down')
  
  // Add text tool click handler
  fabricCanvas.on('mouse:down', (e) => {
    // Only handle left-click
    if (e.e.button !== 0 || isRightClickMode.value) return
    
    const pointer = fabricCanvas.getPointer(e.e)
    showTextInput(pointer.x, pointer.y)
  })
  
  // Optional: Show text cursor more clearly
  fabricCanvas.hoverCursor = 'text'
}

const setupLineTool = () => {
  if (!fabricCanvas) return
  
  let line = null
  let startPoint = null
  
  const onMouseDown = (e) => {
    if (isRightClickMode.value || e.e.button === 2 || e.e.button !== 0) return
    
    const pointer = fabricCanvas.getPointer(e.e)
    startPoint = pointer
    
    line = new fabric.Line([pointer.x, pointer.y, pointer.x, pointer.y], {
      stroke: strokeColor.value,
      strokeWidth: strokeWidth.value,
      strokeUniform: true,
      selectable: true,
      _remote: false,
      _isDrawing: true
    })
    
    fabricCanvas.add(line)
    fabricCanvas.setActiveObject(line)
  }
  
  const onMouseMove = (e) => {
    console.log('on the double')
    if (!line || !line._isDrawing) return
    
    const pointer = fabricCanvas.getPointer(e.e)
    line.set({ x2: pointer.x, y2: pointer.y })
    fabricCanvas.renderAll()
  }
  
  const onMouseUp = () => {
    if (rect && rect._isDrawing) {
        // Ensure minimum dimensions before sending
        if (rect.width < 5 || rect.height < 5) {
        fabricCanvas.remove(rect)
        notificationStore.info('Shape too small', 'Please draw a larger shape')
        } else {
        rect._isDrawing = false
        console.log('Rectangle drawn:', { width: rect.width, height: rect.height })
        }
        
        rect = null
        startPoint = null
        
        setTimeout(() => {
        if (activeTool.value === 'rectangle') {
            selectTool('select')
        }
        }, 50)
    }
    }
  
  // Clean up and set new listeners
  fabricCanvas.off('mouse:down')
  fabricCanvas.off('mouse:move')
  fabricCanvas.off('mouse:up')
  
  fabricCanvas.on('mouse:down', onMouseDown)
  fabricCanvas.on('mouse:move', onMouseMove)
  fabricCanvas.on('mouse:up', onMouseUp)
}

// Update rectangle tool similarly
// Replace the setupRectangleTool function with this fixed version
const setupRectangleTool = () => {
  if (!fabricCanvas) return
  
  let rect = null
  let startPoint = null
  
  const onMouseDown = (e) => {
    if (isRightClickMode.value || e.e.button === 2 || e.e.button !== 0) return
    
    const pointer = fabricCanvas.getPointer(e.e)
    startPoint = pointer
    
    rect = new fabric.Rect({
      left: pointer.x,
      top: pointer.y,
      width: 0,
      height: 0,
      stroke: strokeColor.value,
      strokeWidth: strokeWidth.value,
      fill: fillEnabled.value ? fillColor.value : 'transparent',
      strokeUniform: true,
      selectable: true,
      _remote: false,
      _isDrawing: true,
      id: `rect_${Date.now()}_${Math.random().toString(36).substr(2, 9)}` // Add unique ID
    })
    
    fabricCanvas.add(rect)
    fabricCanvas.setActiveObject(rect)
  }
  
  const onMouseMove = (e) => {
    console.log('on the double 2')
    if (!rect || !rect._isDrawing) return
    
    const pointer = fabricCanvas.getPointer(e.e)
    const width = pointer.x - startPoint.x
    const height = pointer.y - startPoint.y
    
    rect.set({
      width: Math.abs(width),
      height: Math.abs(height),
      left: width > 0 ? startPoint.x : pointer.x,
      top: height > 0 ? startPoint.y : pointer.y
    })
    
    fabricCanvas.renderAll()
  }
  
  const onMouseUp = () => {
    if (rect && rect._isDrawing) {
      rect._isDrawing = false
      
      // CRITICAL: Ensure minimum dimensions and send to server
      if (rect.width >= 5 && rect.height >= 5 && !rect._alreadySent) {
        rect._alreadySent = true
        console.log('Rectangle completed, sending to server:')
        saveToHistory('add', rect)
        sendObjectToServer(rect, 'add')
        } else {
        fabricCanvas.remove(rect)
        notificationStore.info('Shape too small', 'Please draw a larger shape')
      }
      
      rect = null
      startPoint = null
      
      // Auto-switch back to select tool
      setTimeout(() => {
        if (activeTool.value === 'rectangle') {
          selectTool('select')
        }
      }, 50)
    }
  }
  
  fabricCanvas.off('mouse:down')
  fabricCanvas.off('mouse:move')
  fabricCanvas.off('mouse:up')
  
  fabricCanvas.on('mouse:down', onMouseDown)
  fabricCanvas.on('mouse:move', onMouseMove)
  fabricCanvas.on('mouse:up', onMouseUp)
}

// Replace the setupCircleTool function with this fixed version
const setupCircleTool = () => {
  if (!fabricCanvas) return
  
  let circle = null
  let startPoint = null
  
  const onMouseDown = (e) => {
    if (isRightClickMode.value || e.e.button === 2 || e.e.button !== 0) return
    
    const pointer = fabricCanvas.getPointer(e.e)
    startPoint = pointer
    
    circle = new fabric.Circle({
      left: pointer.x,
      top: pointer.y,
      radius: 0,
      stroke: strokeColor.value,
      strokeWidth: strokeWidth.value,
      fill: fillEnabled.value ? fillColor.value : 'transparent',
      strokeUniform: true,
      selectable: true,
      _remote: false,
      _isDrawing: true,
      id: `circle_${Date.now()}_${Math.random().toString(36).substr(2, 9)}` // Add unique ID
    })
    
    fabricCanvas.add(circle)
    fabricCanvas.setActiveObject(circle)
  }
  
  const onMouseMove = (e) => {
    console.log('on the double 3')
    if (!circle || !circle._isDrawing) return
    
    const pointer = fabricCanvas.getPointer(e.e)
    const radius = Math.sqrt(
      Math.pow(pointer.x - startPoint.x, 2) +
      Math.pow(pointer.y - startPoint.y, 2)
    )
    
    circle.set({
      radius: radius,
      left: startPoint.x - radius,
      top: startPoint.y - radius
    })
    
    fabricCanvas.renderAll()
  }
  
  const onMouseUp = () => {
    if (circle && circle._isDrawing) {
      circle._isDrawing = false
      
      // CRITICAL: Ensure minimum radius and send to server
      if (circle.radius >= 5) {
        console.log('Circle completed, sending to server:', circle)
        saveToHistory('add', circle)
        sendObjectToServer(circle, 'add')
      } else {
        fabricCanvas.remove(circle)
        notificationStore.info('Shape too small', 'Please draw a larger shape')
      }
      
      circle = null
      startPoint = null
      
      // Auto-switch back to select tool
      setTimeout(() => {
        if (activeTool.value === 'circle') {
          selectTool('select')
        }
      }, 50)
    }
  }
  
  fabricCanvas.off('mouse:down')
  fabricCanvas.off('mouse:move')
  fabricCanvas.off('mouse:up')
  
  fabricCanvas.on('mouse:down', onMouseDown)
  fabricCanvas.on('mouse:move', onMouseMove)
  fabricCanvas.on('mouse:up', onMouseUp)
}


const setupEraserTool = () => {
  if (!fabricCanvas) return
  
  fabricCanvas.isDrawingMode = false
  fabricCanvas.selection = false
  fabricCanvas.defaultCursor = 'not-allowed'
  
  let isErasing = false
  
  fabricCanvas.off('mouse:down')
  fabricCanvas.off('mouse:move')
  fabricCanvas.off('mouse:up')
  
  fabricCanvas.on('mouse:down', (e) => {
    if (isRightClickMode.value || e.e.button === 2) return
    
    isErasing = true
    eraseAtPoint(e)
  })
  
  fabricCanvas.on('mouse:move', (e) => {
    console.log('on the double 4')
    if (!isErasing) return
    eraseAtPoint(e)
  })
  
  fabricCanvas.on('mouse:up', () => {
    isErasing = false
  })
}

const eraseAtPoint = (e) => {
  const pointer = fabricCanvas.getPointer(e.e)
  const eraserSize = strokeWidth.value * 2
  
  const objects = fabricCanvas.getObjects()
  objects.forEach(obj => {
    if (obj.selectable && !obj._remote) {
      if (obj.type === 'circle' || obj.type === 'ellipse') {
        const dx = pointer.x - (obj.left + obj.radius)
        const dy = pointer.y - (obj.top + obj.radius)
        const distance = Math.sqrt(dx * dx + dy * dy)
        
        if (distance < obj.radius + eraserSize) {
          fabricCanvas.remove(obj)
        }
      }
      else if (obj.left <= pointer.x && pointer.x <= obj.left + obj.width &&
               obj.top <= pointer.y && pointer.y <= obj.top + obj.height) {
        fabricCanvas.remove(obj)
      }
    }
  })
}

// Grid Drawing
const drawGrid = () => {
  if (!fabricCanvas || !showGrid.value) return
  
  // Remove existing grid
  const objects = fabricCanvas.getObjects()
  objects.forEach(obj => {
    if (obj._isGrid) {
      fabricCanvas.remove(obj)
    }
  })
  
  const width = fabricCanvas.width
  const height = fabricCanvas.height
  const gridLines = []
  
  // Draw vertical lines
  for (let x = 0; x <= width; x += gridSize) {
    const line = new fabric.Line([x, 0, x, height], {
      stroke: 'rgba(0, 0, 0, 0.1)',
      strokeWidth: 1,
      selectable: false,
      evented: false,
      _isGrid: true
    })
    gridLines.push(line)
  }
  
  // Draw horizontal lines
  for (let y = 0; y <= height; y += gridSize) {
    const line = new fabric.Line([0, y, width, y], {
      stroke: 'rgba(0, 0, 0, 0.1)',
      strokeWidth: 1,
      selectable: false,
      evented: false,
      _isGrid: true
    })
    gridLines.push(line)
  }
  
  // Add all grid lines to back
  gridLines.forEach(line => {
    fabricCanvas.add(line)
    // Send to back using correct method
    fabricCanvas.sendToBack(line)
  })
}

const toggleGrid = () => {
  showGrid.value = !showGrid.value
  
  if (!fabricCanvas) return
  
  if (showGrid.value) {
    drawGrid()
  } else {
    const objects = fabricCanvas.getObjects()
    objects.forEach(obj => {
      if (obj._isGrid) {
        fabricCanvas.remove(obj)
      }
    })
  }
  
  fabricCanvas.renderAll()
}

const toggleSnap = () => {
  snapToGrid.value = !snapToGrid.value
}

// Text Tool
const showTextInput = (x, y) => {
  textInputActive.value = true
  textInput.value = ''
  textPosition.value = { x, y }
  
  nextTick(() => {
    if (textInputField.value) {
      textInputField.value.focus()
    }
  })
}

// Replace the addText function with this improved version
const addText = () => {
  if (!textInput.value.trim() || !fabricCanvas) return
  
  const text = new fabric.Textbox(textInput.value, {
    left: textPosition.value.x,
    top: textPosition.value.y,
    fontSize: 20,
    fill: strokeColor.value,
    textAlign: 'left',
    selectable: true,
    editable: true,
    _remote: false,
    id: `text_${Date.now()}_${Math.random().toString(36).substr(2, 9)}` // Add unique ID
  })
  
  fabricCanvas.add(text)
  fabricCanvas.setActiveObject(text)
  fabricCanvas.renderAll()
  
  // Send to server
  saveToHistory('add', text)
  sendObjectToServer(text, 'add')
  
  textInputActive.value = false
  textInput.value = ''
  selectTool('select')
}

// Fix the text tool click handler in setupCanvasEvents
if(fabricCanvas){
    fabricCanvas.on('mouse:down', (e) => {
  if (activeTool.value === 'text' && e.e.button === 0) {
    const pointer = fabricCanvas.getPointer(e.e)
    showTextInput(pointer.x, pointer.y)
  }
})
}




const cancelText = () => {
  textInputActive.value = false
  textInput.value = ''
  selectTool('select')
}

// Color & Style Management
const setColor = (color) => {
  strokeColor.value = color
  if (fabricCanvas && fabricCanvas.freeDrawingBrush) {
    fabricCanvas.freeDrawingBrush.color = color
  }
}

const setStrokeWidth = () => {
  if (fabricCanvas && fabricCanvas.freeDrawingBrush) {
    fabricCanvas.freeDrawingBrush.width = strokeWidth.value
  }
}

const setFillColor = (color) => {
  fillColor.value = color
}

const toggleFill = () => {
  fillEnabled.value = !fillEnabled.value
}

// Zoom & Pan
const zoomIn = () => {
  zoom.value = Math.min(zoom.value * 1.2, 5)
  applyZoom()
}

const zoomOut = () => {
  zoom.value = Math.max(zoom.value / 1.2, 0.2)
  applyZoom()
}

const resetZoom = () => {
  zoom.value = 1
  applyZoom()
}

const applyZoom = () => {
  if (!fabricCanvas) return
  
  fabricCanvas.setZoom(zoom.value)
  fabricCanvas.renderAll()
}

// Stickers
const addSticker = (sticker) => {
  if (!fabricCanvas) return
  
  const text = new fabric.Text(sticker.emoji, {
    left: fabricCanvas.width / 2,
    top: fabricCanvas.height / 2,
    fontSize: 40,
    selectable: true,
    _remote: false
  })
  
  fabricCanvas.add(text)
  fabricCanvas.setActiveObject(text)
}

// User Name Change
const updateUserName = () => {
  if (!newUserName.value.trim()) return
  
  const oldName = props.userName
  const newName = newUserName.value.trim()
  
  // Update in localStorage
  const storedUser = JSON.parse(localStorage.getItem(`whiteboard_user_${props.boardId}`) || '{}')
  storedUser.userName = newName
  localStorage.setItem(`whiteboard_user_${props.boardId}`, JSON.stringify(storedUser))
  
  // Send to server
  if (props.socket && props.socket.readyState === WebSocket.OPEN) {
    props.socket.send(JSON.stringify({
      type: 'update_user',
      oldName: oldName,
      newName: newName,
      userId: props.userId
    }))
  }
  
  showNameChange.value = false
  newUserName.value = ''
  notificationStore.success('Name Updated', `Your name is now ${newName}`)
  
  // Emit event to parent to update
  emit('user-name-changed', newName)
}

// WebSocket Communication
// Enhance the sendObjectToServer function
const sendObjectToServer = (object, action) => {
  if (!props.socket || props.socket.readyState !== WebSocket.OPEN) {
    console.warn('WebSocket not connected')
    return
  }
  
  try {
    // CRITICAL: Ensure object has an ID
    if (!object.id) {
      object.id = `obj_${Date.now()}_${Math.random().toString(36).substr(2, 9)}`
    }
    
    // Convert to plain object
    const objectData = object.toObject()
    
    // CRITICAL FIX: ALWAYS include the ID in objectData
    objectData.id = object.id
    
    // Add user metadata
    objectData.userId = props.userId
    objectData.userColor = props.userColor
    objectData.userName = props.userName
    
    // Clean up non-serializable properties
    delete objectData._remote
    delete objectData._isDrawing
    delete objectData._alreadySent
    
    const decidedAction = action === 'add' ? 'add_object' : 
                         action === 'modify' ? 'modify_object' : 
                         'remove_object'
    
    const message = {
      type: decidedAction,
      object: objectData,  // Now always has ID
      object_id: object.id
    }    
    
    console.log('📤 Sending WebSocket:', message.type, objectData.type, objectData.id)
    props.socket.send(JSON.stringify(message))
    
  } catch (error) {
    console.error('❌ Failed to send object:', error)
  }
}

const handleWebSocketMessage = (data) => {
  console.log('📨 Received WebSocket:', data.type, data)
  
  switch (data.type) {
    case 'object_added':
      console.log('🟢 Adding remote object:', data.object?.type, 'from:', data.object?.userName)
      addRemoteObject(data.object)
      break
      
    case 'object_modified':
      console.log('🟡 Modifying remote object:', data.object_id,data.object)
    //   data.object.id = data.object_id
      modifyRemoteObject(data.object,data.object_id)
      break
      
    case 'clear_board':
      console.log('🗑️ Board cleared by:', data.user_name)
    //   alert('object is cleared')
      // Handle remote board clearing
      if (fabricCanvas && data.boardId == props.boardId) {
        fabricCanvas.clear()
        history.value = []
        historyIndex.value = -1
        notificationStore.info('Board Cleared', `${data.user_name} cleared the whiteboard`)
      }
      break
    
    case 'object_removed':
      console.log('🔴 Removing remote object:', data.object_id)
      removeRemoteObject(data.object_id)
      break
    case 'cursor_moved':
      console.log('🎯 CURSOR MOVED received:', {
        user: data.user_name,
        userId: data.user_id,
        position: data.position,
        color: data.user_color
      })
      updateLiveCursor(data)
      
      break
      
    default:
      console.log('⚪ Unknown message type:', data.type)
  }
}


// Replace the addRemoteObject function with this improved version



const addRemoteObject = (objectData) => {
  if (!fabricCanvas || !objectData) return
  
  // Don't add if it's from current user
  if (objectData.userId === props.userId) {
    console.log('Skipping own object:', objectData.userId, props.userId)
    return
  }
  
  console.log('Processing remote object:', objectData.type, 'id:', objectData.id, 'from user:', objectData.userId)
  
  // Check if an object with the same ID already exists
  const existingObjects = fabricCanvas.getObjects()
  let duplicateFound = false
  let duplicateIndex = -1
  let duplicateObject = null
  
  for (let i = 0; i < existingObjects.length; i++) {
    const obj = existingObjects[i]
    // Check both obj.id and obj.toObject().id for comparison
    const objId = obj.id || (obj.toObject && obj.toObject().id)
    if (objId && objId === objectData.id && obj._userId === objectData.userId) {
      duplicateFound = true
      duplicateIndex = i
      duplicateObject = obj
      console.log(`⚠️ Found duplicate object with ID: ${objectData.id} at index ${i}`)
      break
    }
  }
  
  // If duplicate found, remove the old one before adding the new one
  if (duplicateFound && duplicateObject) {
    console.log(`🗑️ Removing duplicate object: ${objectData.id}`)
    
    // Store the z-index of the old object
    const oldZIndex = duplicateIndex
    
    // Remove the old object
    fabricCanvas.remove(duplicateObject)
    
    console.log(`✅ Old duplicate removed, proceeding to add new object at z-index ${oldZIndex}`)
  }
  
  try {
    // Clean up problematic properties that cause rendering issues
    const cleanedData = { ...objectData }
    
    // Remove problematic properties for clean rendering
    delete cleanedData.strokeDashArray  // Remove dashed lines
    delete cleanedData.shadow          // Remove shadows that might cause issues
    delete cleanedData._remote
    delete cleanedData._isDrawing
    
    // Ensure proper stroke properties
    if (cleanedData.type === 'rect' || cleanedData.type === 'circle') {
      cleanedData.strokeLineCap = 'round'
      cleanedData.strokeLineJoin = 'round'
      cleanedData.strokeUniform = true
    }
    
    fabric.util.enlivenObjects([cleanedData], (objects) => {
      objects.forEach(obj => {
        obj._remote = true
        obj._userId = objectData.userId
        obj._userColor = objectData.userColor
        obj.id = objectData.id  // Ensure ID is set on the object
        
        // Make it visible but not interactive for other users
        obj.selectable = false
        obj.evented = false
        
        // Add subtle user identification without breaking the shape
        if (objectData.userColor && obj.type !== 'path') {
          // Add a subtle border or indicator
          obj.set({
            stroke: objectData.stroke || objectData.userColor,  // Use original stroke color
            strokeWidth: objectData.strokeWidth || 2,
            // Remove any dash arrays that cause broken appearance
            strokeDashArray: null
          })
        }
        
        // Add to canvas
        fabricCanvas.add(obj)
        
        // If we removed a duplicate, try to maintain the same z-index
        if (duplicateFound && duplicateIndex !== -1) {
          // Get current index of the newly added object
          const currentIndex = fabricCanvas.getObjects().indexOf(obj)
          const desiredIndex = Math.min(duplicateIndex, fabricCanvas.getObjects().length - 2)
          
          // Move to the position where the old object was
          if (currentIndex !== desiredIndex && desiredIndex >= 0) {
            fabricCanvas.moveTo(obj, desiredIndex)
            console.log(`🔄 Moved new object to z-index ${desiredIndex}`)
          }
        }
        
        console.log('✅ Successfully added remote object:', obj.type, 'id:', objectData.id)
      })
      
      fabricCanvas.renderAll()
    })
    
  } catch (error) {
    console.error('❌ Failed to add remote object:', error.message)
    
    // Fallback: Create object manually for problematic cases
    try {
      createObjectManually(objectData)
    } catch (manualError) {
      console.error('❌ Manual creation also failed:', manualError.message)
    }
  }
}

// Add this helper function for manual object creation

const createObjectManually = (objectData) => {
  if (!fabricCanvas) return
  
  let obj = null
  
  switch (objectData.type) {
    case 'rect':
      obj = new fabric.Rect({
        left: objectData.left || 0,
        top: objectData.top || 0,
        width: objectData.width || 50,
        height: objectData.height || 50,
        fill: objectData.fill || 'transparent',
        stroke: objectData.stroke || objectData.userColor || '#000000',
        strokeWidth: objectData.strokeWidth || 2,
        strokeUniform: true,
        strokeLineCap: 'round',
        strokeLineJoin: 'round',
        // Ensure no dash array
        strokeDashArray: null
      })
      break
      
    case 'circle':
      obj = new fabric.Circle({
        left: objectData.left || 0,
        top: objectData.top || 0,
        radius: objectData.radius || 25,
        fill: objectData.fill || 'transparent',
        stroke: objectData.stroke || objectData.userColor || '#000000',
        strokeWidth: objectData.strokeWidth || 2,
        strokeUniform: true,
        strokeLineCap: 'round',
        strokeLineJoin: 'round',
        // Ensure no dash array
        strokeDashArray: null
      })
      break
      
    case 'textbox':
    case 'text':
      obj = new fabric.Textbox(objectData.text || 'Text', {
        left: objectData.left || 0,
        top: objectData.top || 0,
        fontSize: objectData.fontSize || 20,
        fill: objectData.fill || '#000000',
        textAlign: objectData.textAlign || 'left'
      })
      break
  }
  
  if (obj) {
    obj._remote = true
    obj._userId = objectData.userId
    obj._userColor = objectData.userColor
    obj.id = objectData.id
    
    obj.selectable = false
    obj.evented = false
    
    fabricCanvas.add(obj)
    fabricCanvas.renderAll()
    console.log('✅ Manually created object:', obj.type)
  }
}

// Helper function to create path objects manually


const modifyRemoteObject = (objectData, passedID) => {
  if (!fabricCanvas || objectData.userId === props.userId) return
//   debugObjectModification(objectData, passedID) // Add this line
  console.log('🔧 Modifying remote object:', passedID, objectData.type)
  objectData.id = passedID
  const objects = fabricCanvas.getObjects()
  let target = null
  let targetIndex = -1
  // Find the existing object by ID
  // Try multiple ways to find the object
  for (let i = 0; i < objects.length; i++) {
    const obj = objects[i]
    if (obj._remote) {
      const objId = obj.id || obj.toObject().id
      if (objId == passedID) {
        target = obj
        targetIndex = i
        break
      }
    }
  }
  
  if (target) {
    console.log('Found existing object to modify:', target)
    
    // Store important properties from the old object
    const oldZIndex = fabricCanvas.getObjects().indexOf(target)
    const oldId = target.id
    const oldRemote = target._remote
    
    // Remove the old object completely
    fabricCanvas.remove(target)
    console.log('Removed old object')
    fabricCanvas.getObjects()
    // Create a new object with the updated data
    const newObjectData = { ...objectData }
    newObjectData.id = oldId  // Preserve the original ID
    newObjectData._remote = oldRemote  // Keep it marked as remote
    newObjectData.selectable = false  // Make it non-interactive for remote users
    newObjectData.evented = false
    
    // Create the new object based on type
    let newObject = null
    
    switch (objectData.type) {
      case 'rect':
        newObject = new fabric.Rect(objectData.path,{
          left: objectData.left,
          top: objectData.top,
          width: objectData.width,
          height: objectData.height,
          fill: objectData.fill || 'transparent',
          stroke: objectData.stroke,
          strokeWidth: objectData.strokeWidth,
          strokeUniform: true,
          strokeLineCap: 'round',
          strokeLineJoin: 'round',
          angle: objectData.angle || 0,
          scaleX: objectData.scaleX || 1,
          scaleY: objectData.scaleY || 1,
          opacity: objectData.opacity || 1,
          visible: objectData.visible !== false,
          id: oldId,
          _remote: oldRemote,
          selectable: false,
          evented: false
        })
        break
        
      case 'circle':
        newObject = new fabric.Circle({
          left: objectData.left,
          top: objectData.top,
          radius: objectData.radius,
          fill: objectData.fill || 'transparent',
          stroke: objectData.stroke,
          strokeWidth: objectData.strokeWidth,
          strokeUniform: true,
          strokeLineCap: 'round',
          strokeLineJoin: 'round',
          angle: objectData.angle || 0,
          scaleX: objectData.scaleX || 1,
          scaleY: objectData.scaleY || 1,
          opacity: objectData.opacity || 1,
          visible: objectData.visible !== false,
          id: oldId,
          _remote: oldRemote,
          selectable: false,
          evented: false
        })
        break
        
      case 'path':
        newObject = new fabric.Path(objectData.path, {
          left: objectData.left,
          top: objectData.top,
          fill: objectData.fill || null,
          stroke: objectData.stroke,
          strokeWidth: objectData.strokeWidth,
          strokeLineCap: objectData.strokeLineCap || 'round',
          strokeLineJoin: objectData.strokeLineJoin || 'round',
          angle: objectData.angle || 0,
          scaleX: objectData.scaleX || 1,
          scaleY: objectData.scaleY || 1,
          opacity: objectData.opacity || 1,
          visible: objectData.visible !== false,
          id: oldId,
          _remote: oldRemote,
          selectable: false,
          evented: false
        })
        break
        
      case 'textbox':
      case 'text':
        newObject = new fabric.Textbox(objectData.text || '', {
          left: objectData.left,
          top: objectData.top,
          width: objectData.width,
          height: objectData.height,
          fontSize: objectData.fontSize || 20,
          fill: objectData.fill || '#000000',
          textAlign: objectData.textAlign || 'left',
          angle: objectData.angle || 0,
          scaleX: objectData.scaleX || 1,
          scaleY: objectData.scaleY || 1,
          opacity: objectData.opacity || 1,
          visible: objectData.visible !== false,
          id: oldId,
          _remote: oldRemote,
          selectable: false,
          evented: false
        })
        break
    }
    
    if (newObject) {
      // Insert at the same z-index to maintain layering
      fabricCanvas.insertAt(newObject, oldZIndex, false)
      fabricCanvas.renderAll()
    // console.log('Object not found for modification, adding as new',objectData.userId, props.userId)
    addRemoteObject(objectData)
      console.log('✅ Object replaced successfully at index:', oldZIndex)
    }
  } else {
    console.log('Object not found for modification, adding as new',objectData.userId, props.userId)
    addRemoteObject(objectData)
  }
}


const removeRemoteObject = (objectId) => {
  if (!fabricCanvas || !objectId) return
  
  console.log('🔴 Removing remote object:', objectId)
  
  const objects = fabricCanvas.getObjects().filter(obj => !obj._isGrid)
  console.log(objects)
  const target = objects.find(obj => obj._remote && obj.id === objectId)
  
  if (target) {
    fabricCanvas.remove(target)
    fabricCanvas.renderAll()
    console.log('✅ Remote object removed:', objectId)
  } else {
    console.log('❌ Object not found for removal:', objectId)
  }
}

const updateLiveCursor = (data) => {
  if (!data.user_id || data.user_id === props.userId) return
  
  // Adjust cursor position for zoom
  const cursorX = (data.position?.x || 0) * zoom.value
  const cursorY = (data.position?.y || 0) * zoom.value
  
  liveCursors.value[data.user_id] = {
    x: cursorX,
    y: cursorY,
    color: data.user_color || '#999999',
    name: data.user_name || 'User',
    updatedAt: Date.now()
  }
  
  // Clean up old cursors
  const now = Date.now()
  Object.keys(liveCursors.value).forEach(userId => {
    if (now - liveCursors.value[userId].updatedAt > 5000) {
      delete liveCursors.value[userId]
    }
  })
}

// Import/Export
const exportJSON = () => {
  if (!fabricCanvas) return
  
  const json = fabricCanvas.toJSON()
  const dataStr = JSON.stringify(json, null, 2)
  const dataUri = 'data:application/json;charset=utf-8,' + encodeURIComponent(dataStr)
  
  const exportFileDefaultName = `whiteboard-${props.boardId}-${new Date().toISOString().slice(0, 10)}.json`
  
  const linkElement = document.createElement('a')
  linkElement.setAttribute('href', dataUri)
  linkElement.setAttribute('download', exportFileDefaultName)
  linkElement.click()
  
  notificationStore.success('Exported', 'Whiteboard exported as JSON')
}

// Add this to monitor WebSocket connection
const setupWebSocketListeners = () => {
    
  if (!props.socket) return
  
  props.socket.addEventListener('open', () => {
    console.log('✅ WebSocket connected for cursor tracking')
  })
  
  props.socket.addEventListener('close', () => {
    console.log('❌ WebSocket disconnected')
    liveCursors.value = {} // Clear all cursors on disconnect
  })
  
  props.socket.addEventListener('error', (error) => {
    console.error('❌ WebSocket error:', error)
  })
}

const exportImage = () => {
  if (!fabricCanvas) return
  
  const dataURL = fabricCanvas.toDataURL({
    format: 'png',
    quality: 1
  })
  
  const link = document.createElement('a')
  link.href = dataURL
  link.download = `whiteboard-${props.boardId}-${new Date().toISOString().slice(0, 10)}.png`
  link.click()
  
  notificationStore.success('Exported', 'Whiteboard exported as PNG image')
}

const importJSON = () => {
  const input = document.createElement('input')
  input.type = 'file'
  input.accept = '.json'
  
  input.onchange = (e) => {
    const file = e.target.files[0]
    if (!file) return
    
    const reader = new FileReader()
    reader.onload = (event) => {
      try {
        const json = JSON.parse(event.target.result)
        fabricCanvas.loadFromJSON(json, () => {
          fabricCanvas.renderAll()
          notificationStore.success('Imported', 'Whiteboard imported successfully')
        })
      } catch (error) {
        notificationStore.error('Import Failed', 'Invalid JSON file')
      }
    }
    reader.readAsText(file)
  }
  
  input.click()
}

// Clear Canvas
const clearCanvas = () => {
  if (!fabricCanvas || !confirm('Are you sure you want to clear the entire whiteboard?')) return
  
  console.log('🗑️ Clearing board locally and broadcasting...')
  
//   // Get all objects to remove them individually first
  const objects = fabricCanvas.getObjects().filter(obj => !obj._isGrid)
  console.log(objects)
//   // Remove objects one by one to ensure proper sync
  objects.forEach(obj => {
    if (obj.id) {
      sendObjectToServer(obj, 'remove')
    }
  })
  
  // Clear local canvas
  fabricCanvas.clear()
  history.value = []
  historyIndex.value = -1
  
  // Send clear board message
  if (props.socket && props.socket.readyState === WebSocket.OPEN) {
    const clearMessage = {
      type: 'clear_board',
      user_id: props.userId,
      user_name: props.userName,
      boardId : props.boardId
    }
    console.log('📤 Sending clear board message:', clearMessage)
    props.socket.send(JSON.stringify(clearMessage))
  }
  
  emit('board-cleared')
  notificationStore.info('Cleared', 'Whiteboard cleared')
}

const setupCursorTracking = () => {
  if (!fabricCanvas || !canvasContainer.value) return
  
  let lastCursorSend = 0
  const CURSOR_THROTTLE = 50 // Send cursor updates every 50ms max
  
  // Remove existing event listeners
  canvasContainer.value.removeEventListener('mousemove', handleMouseMove)
  
  // Add new event listener to container
  canvasContainer.value.addEventListener('mousemove', handleMouseMove)
  
  function handleMouseMove(e) {
    console.log('🖱️ Container mouse move detected', e)
    
    if (!props.socket || props.socket.readyState !== WebSocket.OPEN) return
    
    const now = Date.now()
    if (now - lastCursorSend < CURSOR_THROTTLE) return
    
    // Get pointer position relative to canvas
    const rect = canvasContainer.value.getBoundingClientRect()
    const x = e.clientX - rect.left
    const y = e.clientY - rect.top
    
    // Adjust for canvas zoom
    const adjustedX = x / zoom.value
    const adjustedY = y / zoom.value
    
    const cursorData = {
      type: 'cursor_move',
      position: { x: adjustedX, y: adjustedY },
      user_id: props.userId,
      user_name: props.userName,
      user_color: props.userColor
    }
    
    console.log('📤 Sending cursor move from container:', cursorData)
    props.socket.send(JSON.stringify(cursorData))
    lastCursorSend = now
  }
}



// Lifecycle
onMounted(() => {
  nextTick(() => {
    initCanvas()
    loadAutoSave()
    selectTool('select')
  })

  // Debug: Log WebSocket connection
    if (props.socket) {
      console.log('WebSocket passed to FabricWhiteboard:', {
        readyState: props.socket.readyState,
        url: props.socket.url
      })
      setupWebSocketListeners()
    }
  
  
  window.addEventListener('resize', handleResize)
  window.addEventListener('contextmenu', preventContextMenu)
})

onUnmounted(() => {
  if (fabricCanvas) {
    fabricCanvas.dispose()
  }
   // Clean up container event listeners
  if (canvasContainer.value) {
    canvasContainer.value.removeEventListener('mousemove', handleMouseMove)
    if (canvasContainer.value._drawingHandlers) {
      canvasContainer.value.removeEventListener('mousedown', canvasContainer.value._drawingHandlers.mousedown)
      canvasContainer.value.removeEventListener('mousemove', canvasContainer.value._drawingHandlers.mousemove)
      canvasContainer.value.removeEventListener('mouseup', canvasContainer.value._drawingHandlers.mouseup)
    }
  }
  
  window.removeEventListener('resize', handleResize)
  window.removeEventListener('contextmenu', preventContextMenu)
})

const preventContextMenu = (e) => {
  if (e.target === canvas.value) {
    e.preventDefault()
  }
}

const handleResize = () => {
  if (!fabricCanvas || !canvasContainer.value) return
  
  const containerWidth = canvasContainer.value.clientWidth
  const containerHeight = canvasContainer.value.clientHeight
  
  fabricCanvas.setDimensions({
    width: containerWidth,
    height: containerHeight
  })
  
  if (showGrid.value) {
    toggleGrid()
    toggleGrid()
  }
  
  fabricCanvas.renderAll()
}

// Expose methods
defineExpose({
  handleWebSocketMessage,
  clearCanvas: () => {
    if (fabricCanvas) {
      fabricCanvas.clear()
      history.value = []
      historyIndex.value = -1
    }
  }
})
</script>

<style scoped>
.fabric-whiteboard {
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  background: #f5f5f5;
  position: relative;
}

.toolbar {
  background: #2d3748;
  color: white;
  padding: 0.75rem;
  display: flex;
  flex-wrap: wrap;
  gap: 1rem;
  align-items: center;
  border-bottom: 1px solid #4a5568;
  z-index: 10;
}

.toolbar-section {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.25rem;
  border-right: 1px solid #4a5568;
  padding-right: 1rem;
}

.toolbar-section:last-child {
  border-right: none;
}

.toolbar button {
  background: #4a5568;
  border: none;
  color: white;
  padding: 0.5rem 0.75rem;
  border-radius: 0.375rem;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: background 0.2s;
  min-height: 36px;
}

.toolbar button:hover {
  background: #5a6578;
}

.toolbar button.active {
  background: #4299e1;
  box-shadow: 0 0 0 2px rgba(66, 153, 225, 0.5);
}

.toolbar button:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

.color-picker {
  display: flex;
  gap: 0.25rem;
  flex-wrap: wrap;
}

.color-picker button {
  width: 1.5rem;
  height: 1.5rem;
  border-radius: 50%;
  border: 2px solid transparent;
  padding: 0;
  min-height: auto;
}

.color-picker button.active {
  border-color: white;
  transform: scale(1.1);
}

.toolbar input[type="color"] {
  width: 2rem;
  height: 2rem;
  border: none;
  border-radius: 0.375rem;
  cursor: pointer;
  padding: 0;
}

.toolbar input[type="range"] {
  width: 80px;
}

.zoom-level {
  font-size: 0.875rem;
  font-weight: bold;
  min-width: 50px;
  text-align: center;
}

.right-click-toggle {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  font-size: 0.875rem;
}

.right-click-toggle input {
  margin: 0;
}

.canvas-container {
  flex: 1;
  position: relative;
  overflow: hidden;
}

.canvas-container canvas {
  display: block;
  background: white;
  cursor: default;
}

/* Add these styles to your component's style section */
.cursor {
  position: absolute;
  transform: translate(-50%, -50%);
  transition: all 0.1s ease-out;
  pointer-events: none;
  z-index: 1000;
  border: 2px solid red !important; /* Force visible border */
  background-color: rgba(255, 0, 0, 0.1) !important; /* Force background */
}

.cursor-dot {
  width: 12px !important; /* Larger for visibility */
  height: 12px !important;
  border-radius: 50%;
  border: 3px solid white !important;
  box-shadow: 0 0 0 2px rgba(0,0,0,0.5) !important;
}

.cursor-name {
  position: absolute;
  top: 15px !important;
  left: 50%;
  transform: translateX(-50%);
  background: rgba(0, 0, 0, 0.9) !important;
  color: white !important;
  padding: 4px 8px !important;
  border-radius: 4px !important;
  font-size: 12px !important;
  white-space: nowrap !important;
  font-weight: bold !important;
}

.cursors-overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  pointer-events: none;
  z-index: 999;
  /* Add for debugging */
  border: 1px solid blue !important; /* Make overlay visible */
}

.text-input-modal {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 2000;
}

.modal-content {
  background: white;
  padding: 1.5rem;
  border-radius: 0.5rem;
  min-width: 300px;
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.2);
}

.modal-content h3 {
  margin: 0 0 1rem 0;
  color: #2d3748;
}

.modal-content input {
  width: 100%;
  padding: 0.5rem;
  border: 1px solid #cbd5e0;
  border-radius: 0.375rem;
  margin-bottom: 1rem;
}

.modal-actions {
  display: flex;
  gap: 0.5rem;
  justify-content: flex-end;
}

.modal-actions button {
  padding: 0.5rem 1rem;
  border: none;
  border-radius: 0.375rem;
  cursor: pointer;
}

.modal-actions button:first-child {
  background: #4299e1;
  color: white;
}

.modal-actions button:last-child {
  background: #cbd5e0;
  color: #4a5568;
}

.name-change-btn {
  position: absolute;
  top: 70px;
  right: 20px;
  z-index: 100;
}

.name-change-btn button {
  background: rgba(255, 255, 255, 0.9);
  border: 1px solid #cbd5e0;
  border-radius: 0.375rem;
  padding: 0.5rem 1rem;
  display: flex;
  align-items: center;
  font-size: 0.875rem;
  cursor: pointer;
  transition: all 0.2s;
}

.name-change-btn button:hover {
  background: white;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.name-change-modal {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 2000;
}

.name-input {
  width: 100%;
  padding: 0.75rem;
  border: 1px solid #cbd5e0;
  border-radius: 0.375rem;
  margin: 1rem 0;
  font-size: 1rem;
}

.btn-primary {
  background: #4299e1;
  color: white;
  padding: 0.5rem 1rem;
  border: none;
  border-radius: 0.375rem;
  cursor: pointer;
  margin-right: 0.5rem;
}

.btn-secondary {
  background: #cbd5e0;
  color: #4a5568;
  padding: 0.5rem 1rem;
  border: none;
  border-radius: 0.375rem;
  cursor: pointer;
}

.stickers-panel {
  position: absolute;
  top: 60px;
  right: 20px;
  background: white;
  border: 1px solid #cbd5e0;
  border-radius: 0.5rem;
  padding: 1rem;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  z-index: 100;
  max-height: 300px;
  overflow-y: auto;
}

.stickers-panel h3 {
  margin: 0 0 0.5rem 0;
  font-size: 0.875rem;
  color: #4a5568;
}

.stickers-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 0.5rem;
}

.sticker-btn {
  font-size: 1.5rem;
  width: 2.5rem;
  height: 2.5rem;
  display: flex;
  align-items: center;
  justify-content: center;
  border: 1px solid #cbd5e0;
  border-radius: 0.375rem;
  background: white;
  cursor: pointer;
  transition: all 0.2s;
}

.sticker-btn:hover {
  background: #f7fafc;
  transform: scale(1.1);
}

.history-timeline {
  position: absolute;
  bottom: 20px;
  left: 20px;
  background: white;
  border: 1px solid #cbd5e0;
  border-radius: 0.5rem;
  padding: 1rem;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  z-index: 100;
  max-height: 300px;
  overflow-y: auto;
  min-width: 250px;
}

.history-timeline h3 {
  margin: 0 0 0.5rem 0;
  font-size: 0.875rem;
  color: #4a5568;
}

.history-list {
  display: flex;
  flex-direction: column;
  gap: 0.25rem;
}

.history-item {
  padding: 0.5rem;
  border-radius: 0.25rem;
  font-size: 0.75rem;
  cursor: pointer;
  transition: background 0.2s;
}

.history-item:hover {
  background: #f7fafc;
}

.history-item.active {
  background: #4299e1;
  color: white;
}


</style>