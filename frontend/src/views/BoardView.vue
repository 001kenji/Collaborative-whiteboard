<template>
  <div class="min-h-screen bg-gradient-to-br from-gray-900 via-gray-800 to-gray-900">
    <!-- Mobile Top Bar (Hidden on desktop) -->
    <div class="lg:hidden fixed top-0 left-0 right-0 z-50 bg-gray-800/95 backdrop-blur-xl border-b border-gray-700/50">
      <div class="px-4 py-3 flex items-center justify-between">
        <button @click="showMobileSidebar = !showMobileSidebar" 
                class="p-2 rounded-lg bg-gray-700/50 border border-gray-600/50">
          <svg class="w-5 h-5 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16" />
          </svg>
        </button>
        
        <div class="flex items-center gap-3">
          <div class="w-2 h-2 rounded-full animate-pulse" :style="{ backgroundColor: connectionStatusColor }"></div>
          <span class="text-sm font-medium">{{ users.length }}</span>
          <button @click="copyBoardLink" class="p-2 text-blue-400 flex flex-col">
            <svg class="w-5 h-5 mx-auto" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z" />
            </svg>
             <span class="text-xs italic md:text-sm cursor-pointer">Copy Link</span>
          </button>
        </div>
      </div>
    </div>

    <!-- Main Navigation - Desktop -->
    <nav class="hidden lg:block bg-gray-800/50 backdrop-blur-xl border-b border-gray-700/50 text-white shadow-2xl shadow-black/20">
      <div class="container mx-auto px-4 py-3">
        <div class="flex flex-col xl:flex-row justify-between items-center gap-4">
          <!-- Left Section -->
          <div class="flex flex-col md:flex-row items-start md:items-center gap-4 w-full xl:w-auto">
            <router-link to="/" 
                        class="group flex items-center gap-2 px-4 py-2 rounded-xl bg-gradient-to-r from-gray-700/50 to-gray-800/50 
                               hover:from-blue-600/20 hover:to-blue-700/20 border border-gray-600/50 hover:border-blue-500/50 
                               transition-all duration-300 w-full md:w-auto justify-center md:justify-start">
              <svg class="w-5 h-5 group-hover:rotate-180 transition-transform duration-300" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18" />
              </svg>
              <span class="font-medium">Home</span>
            </router-link>
            
            <div class="flex flex-col md:flex-row items-start md:items-center gap-3 md:gap-4 w-full md:w-auto">
              <div class="hidden md:block h-6 w-px bg-gradient-to-b from-gray-600 to-transparent"></div>
              
              <div class="flex flex-col">
                <h1 class="text-lg md:text-xl font-bold bg-gradient-to-r from-blue-400 to-cyan-300 bg-clip-text text-transparent">
                  Whiteboard
                </h1>
                <p class="text-xs md:text-sm text-gray-400">ID: {{ boardId }}</p>
              </div>
            </div>
            
            <div class="flex items-center gap-3 px-4 py-2 rounded-xl bg-gradient-to-r from-gray-700/50 to-gray-800/50 
                        border border-gray-600/50 w-full md:w-auto justify-between md:justify-start">
              <div class="flex items-center gap-2">
                <div class="w-2 h-2 rounded-full bg-gradient-to-r from-green-400 to-emerald-400 animate-pulse"></div>
                <span class="text-sm font-medium hidden sm:inline">You:</span>
              </div>
              <div class="flex items-center gap-2">
                <span class="font-semibold truncate max-w-[120px] sm:max-w-none">{{ userDisplayName }}</span>
                <button @click="showNameChange = true" 
                        class="p-1 hover:bg-gray-600/30 rounded-lg transition-all duration-200 hover:scale-110"
                        title="Change name">
                  <svg class="w-4 h-4 text-blue-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" 
                          d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z" />
                  </svg>
                </button>
              </div>
            </div>
          </div>
          
          <!-- Right Section -->
          <div class="flex flex-col sm:flex-row items-stretch sm:items-center gap-3 md:gap-6 w-full xl:w-auto">
            <!-- Connection Status -->
            <div class="flex items-center gap-3 px-4 py-2 rounded-xl bg-gradient-to-r from-gray-700/50 to-gray-800/50 
                        border border-gray-600/50 justify-between sm:justify-start">
              <div class="flex items-center gap-2">
                <div class="w-3 h-3 rounded-full animate-pulse" :style="{ backgroundColor: connectionStatusColor }"></div>
                <span class="text-sm font-medium hidden sm:inline">{{ connectionStatus }}</span>
              </div>
            </div>
            
            <!-- Copy Link Button -->
            <button
              @click="copyBoardLink"
              class="group px-4 lg:px-5 py-2 lg:py-2.5 bg-gradient-to-r from-blue-600 to-blue-700 hover:from-blue-500 hover:to-blue-600 
                     rounded-xl transition-all duration-300 shadow-lg shadow-blue-500/20 hover:shadow-blue-500/30
                     border border-blue-500/30 flex items-center justify-center gap-2 font-medium w-full sm:w-auto"
            >
              <svg class="w-5 h-5 group-hover:rotate-12 transition-transform duration-300 hidden sm:inline" 
                   fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" 
                      d="M13 10V3L4 14h7v7l9-11h-7z" />
              </svg>
              <span class="text-xs ">Copy Link</span>
            </button>
            
            <!-- Participants -->
            <div class="flex items-center justify-between sm:justify-start gap-4 px-4 py-2 rounded-xl bg-gradient-to-r from-gray-700/50 to-gray-800/50 
                        border border-gray-600/50">
              <span class="text-sm font-medium hidden md:inline">Participants</span>
              <div class="flex items-center gap-3">
                <div class="flex -space-x-3">
                  <div
                    v-for="user in users.slice(0, 3)"
                    :key="user.id"
                    class="w-8 h-8 md:w-9 md:h-9 rounded-full border-3 border-gray-800 flex items-center justify-center 
                           text-xs md:text-sm font-bold shadow-lg"
                    :style="{ backgroundColor: user.color }"
                    :title="user.name"
                  >
                    {{ userInitial(user.name) }}
                  </div>
                  <div v-if="users.length > 3" 
                       class="w-8 h-8 md:w-9 md:h-9 rounded-full border-3 border-gray-800 bg-gray-700 
                              flex items-center justify-center text-xs md:text-sm font-bold shadow-lg">
                    +{{ users.length - 3 }}
                  </div>
                </div>
                <span class="px-3 py-1 bg-gray-700/50 rounded-full text-sm font-semibold border border-gray-600/50">
                  {{ users.length }}
                </span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </nav>
    
    <!-- Mobile Sidebar Drawer -->
    <div v-if="showMobileSidebar" 
         class="lg:hidden fixed inset-0 z-50 bg-black/60 backdrop-blur-sm"
         @click="showMobileSidebar = false">
         
      <div class="absolute top-16 bottom-0 left-0 w-72 bg-gradient-to-b from-gray-800 to-gray-900 
                  border-r border-gray-700/50 shadow-2xl overflow-y-auto"
           @click.stop>
           <button @click="showNameChange = true"
                  class="mt-6 w-[85%] mx-auto px-4 py-2 bg-gradient-to-r from-blue-600/20 to-blue-700/20 
                         hover:from-blue-600/30 hover:to-blue-700/30 border border-blue-500/30 
                         rounded-xl font-medium transition-all duration-300 flex items-center justify-center gap-2">
            <svg class="w-5 h-5 text-blue-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" 
                    d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z" />
            </svg>
            Change Name
          </button>

          
        <div class="p-6">

          <div class="mt-8 pb-6 border-b border-gray-700/50">
            <div class="flex items-center justify-between text-sm">
              <span class="text-gray-400">Board ID:</span>
              <span @click="copyBoardLink" class="font-mono text-blue-300">{{ boardId }}</span>
            </div>
            <div class="mt-2 flex items-center justify-between text-sm">
              <span class="text-gray-400">Status:</span>
              <span class="text-green-300">Connected</span>
            </div>
          </div>


          <div class="flex items-center gap-3 mt-2 mb-5">
            <h2 class="text-md font-bold bg-gradient-to-r from-blue-400 to-cyan-300 bg-clip-text text-transparent">
              Participants ({{ users.length }})
            </h2>
          </div>
          
          <div class="space-y-3">
            <div
              v-for="user in users"
              :key="user.id"
              class="group p-2 rounded-xl bg-gradient-to-r from-gray-700/30 to-gray-800/30 
                     border border-gray-600/30 transition-all duration-300"
            >
              <div class="flex items-center gap-4">
                <div class="relative">
                  <div class="w-8 h-8 rounded-full flex items-center justify-center text-sm font-bold shadow-lg"
                       :style="{ backgroundColor: user.color }">
                    {{ userInitial(user.name) }}
                  </div>
                </div>
                
                <div class="flex-1 min-w-0">
                  <div class="flex items-center gap-2">
                    <p class="font-semibold text-xs text-white truncate">{{ user.name }}</p>
                    <div v-if="user.id === currentUserId" 
                         class="px-2 py-1 bg-gradient-to-r from-blue-500/20 to-blue-600/20 text-blue-300 
                                text-xs font-medium rounded-lg border border-blue-500/30">
                      You
                    </div>
                  </div>
                  <p class="text-xs text-gray-400 mt-1">Joined {{ formatTime(user.joined_at) }}</p>
                </div>
              </div>
            </div>
          </div>
          
          
          
          
        </div>
      </div>
    </div>
    
    <!-- Name Change Modal -->
    <div v-if="showNameChange" class="fixed inset-0 bg-black/60 backdrop-blur-sm flex items-center justify-center z-50 p-4">
      <div class="bg-gradient-to-br from-gray-800 to-gray-900 p-6 md:p-8 rounded-2xl shadow-2xl shadow-black/40 
                  border border-gray-700/50 max-w-md w-full mx-auto">
        <div class="flex items-center gap-3 mb-6">
          <div class="p-2 bg-gradient-to-br from-blue-500/20 to-blue-600/20 rounded-xl">
            <svg class="w-5 h-5 md:w-6 md:h-6 text-blue-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" 
                    d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z" />
            </svg>
          </div>
          <h3 class="text-lg md:text-xl font-bold bg-gradient-to-r from-blue-400 to-cyan-300 bg-clip-text text-transparent">
            Change Your Name
          </h3>
        </div>
        
        <input
          v-model="newUserName"
          @keyup.enter="updateUserName"
          placeholder="Enter your new name"
          class="w-full px-4 py-3 bg-gray-700/50 border border-gray-600/50 rounded-xl focus:border-blue-500/50 
                 focus:ring-2 focus:ring-blue-500/30 focus:outline-none transition-all duration-300
                 text-white placeholder-gray-400"
          autofocus
        />
        
        <div class="flex flex-col sm:flex-row justify-end gap-3 mt-8">
          <button @click="showNameChange = false" 
                  class="px-5 py-2.5 bg-gray-700/50 hover:bg-gray-600/50 border border-gray-600/50 
                         rounded-xl font-medium transition-all duration-300 order-2 sm:order-1">
            Cancel
          </button>
          <button @click="updateUserName" 
                  class="px-5 py-2.5 bg-gradient-to-r from-blue-600 to-blue-700 hover:from-blue-500 hover:to-blue-600 
                         rounded-xl font-medium shadow-lg shadow-blue-500/20 hover:shadow-blue-500/30
                         border border-blue-500/30 transition-all duration-300 order-1 sm:order-2 mb-3 sm:mb-0">
            Update Name
          </button>
        </div>
      </div>
    </div>
    
    <!-- Main Content Area -->
    <div class="flex flex-col lg:flex-row h-screen pt-16 lg:pt-0">
      <!-- Sidebar - Desktop -->
      <div class="hidden lg:block w-full lg:w-72 xl:w-80 bg-gray-800/30 backdrop-blur-xl border-r border-gray-700/50 
                  text-white overflow-y-auto flex-shrink-0">
        <div class="p-6">
          <div class="flex items-center gap-3 mb-8">
            <div class="p-2 bg-gradient-to-br from-blue-500/20 to-blue-600/20 rounded-xl">
              <svg class="w-5 h-5 text-blue-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" 
                      d="M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197m13.5 0h-15" />
              </svg>
            </div>
            <h2 class="text-md xl:text-lg font-bold bg-gradient-to-r from-blue-400 to-cyan-300 bg-clip-text text-transparent">
              Active Participants
            </h2>
            <span class="ml-auto px-3 py-1 bg-gray-700/50 rounded-full text-sm font-semibold border border-gray-600/50">
              {{ users.length }}
            </span>
          </div>
          
          <div class="space-y-3">
            <div
              v-for="user in users"
              :key="user.id"
              class="group p-4 rounded-xl bg-gradient-to-r from-gray-700/30 to-gray-800/30 hover:from-gray-600/40 hover:to-gray-700/40 
                     border border-gray-600/30 hover:border-blue-500/30 transition-all duration-300 cursor-pointer"
            >
              <div class="flex items-center gap-2">
                <div class="relative">
                  <div class="absolute inset-0 bg-gradient-to-br from-current to-transparent opacity-20 blur-md rounded-full"></div>
                  <div class="relative w-8 h-8  rounded-full flex items-center justify-center text-sm font-bold shadow-lg"
                       :style="{ backgroundColor: user.color }">
                    {{ userInitial(user.name) }}
                  </div>
                </div>
                
                <div class="flex-1 min-w-0">
                  <div class="flex items-center gap-2">
                    <p class="font-semibold text-xs text-white truncate">{{ user.name }}</p>
                    <div v-if="user.id === currentUserId" 
                         class="px-2 py-1 bg-gradient-to-r from-blue-500/20 to-blue-600/20 text-blue-300 
                                text-xs font-medium rounded-lg border border-blue-500/30">
                      You
                    </div>
                  </div>
                  <p class="text-xs text-gray-400 mt-1">Joined {{ formatTime(user.joined_at) }}</p>
                </div>
                
                <div class="w-2 h-2 rounded-full bg-gradient-to-r from-green-400 to-emerald-400 animate-pulse"></div>
              </div>
            </div>
          </div>
          
          <!-- Sidebar Footer -->
          <div class="mt-8 pt-6 border-t border-gray-700/50">
            <div class="flex items-center justify-between text-sm">
              <span class="text-gray-400">Board ID:</span>
              <span class="font-mono text-blue-300 truncate">{{ boardId }}</span>
            </div>
            <div class="mt-2 flex items-center justify-between text-sm">
              <span class="text-gray-400">Last Updated:</span>
              <span class="text-gray-300">{{ formatTime(new Date()) }}</span>
            </div>
          </div>
        </div>
      </div>
      
      <!-- Whiteboard Area -->
      <div class="flex-1 relative min-h-0">
        <div class="absolute inset-0">
          <FabricWhiteboard
            :board-id="boardId"
            :user-id="currentUserId"
            :user-name="userDisplayName"
            :user-color="currentUserColor"
            :socket="socket"
            @update-users="updateUsersList"
            @board-cleared="handleBoardCleared"
            @user-name-changed="handleUserNameChanged"
            ref="whiteboardRef"
          />
        </div>
        
        <!-- Connection Status Overlay -->
        <div v-if="!isConnected" class="absolute inset-0 bg-black/80 backdrop-blur-sm flex items-center justify-center p-4">
          <div class="text-center p-8 bg-gradient-to-br from-gray-800 to-gray-900 rounded-2xl 
                      border border-gray-700/50 shadow-2xl shadow-black/40 max-w-md w-full">
            <div class="relative mb-6">
              <div class="absolute inset-0 bg-gradient-to-r from-blue-500/20 to-cyan-500/20 blur-xl rounded-full"></div>
              <div class="relative animate-spin rounded-full h-16 w-16 border-b-2 border-t-2 border-blue-500 mx-auto">
                <div class="absolute inset-2 rounded-full border-2 border-blue-300/30"></div>
              </div>
            </div>
            <h3 class="text-lg md:text-xl font-bold text-white mb-2">Connecting to Whiteboard</h3>
            <p class="text-gray-300 mb-6 text-sm md:text-base">Establishing secure connection...</p>
            <div class="inline-flex items-center gap-2 px-4 py-2 bg-gray-700/50 rounded-xl border border-gray-600/50">
              <div class="w-2 h-2 rounded-full bg-gradient-to-r from-yellow-400 to-orange-400 animate-pulse"></div>
              <span class="text-sm font-medium">Connecting...</span>
            </div>
          </div>
        </div>
        
        


      </div>
    </div>
  </div>
</template>


<script setup>
import { ref, onMounted, onUnmounted, computed, nextTick } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { useWhiteboardStore } from '@/stores/whiteboard'
import { push } from 'notivue'
import FabricWhiteboard from '@/components/FabricWhiteboard.vue'

const route = useRoute()
const router = useRouter()
const whiteboardStore = useWhiteboardStore()
const notificationStore = push
const whiteboardRef = ref(null)
const showMobileSidebar = ref(false)
const boardId = route.params.id
const socket = ref(null)
const isConnected = ref(false)
const userDisplayName = ref('')
const userSessionId = ref('')
const showNameChange = ref(false)
const newUserName = ref('')

const connectionStatus = computed(() => isConnected.value ? 'Connected' : 'Connecting...')
const connectionStatusColor = computed(() => isConnected.value ? '#10B981' : '#F59E0B')
const users = computed(() => whiteboardStore.currentBoard?.users || [])
const currentUserId = computed(() => whiteboardStore.currentUserId)
const currentUserColor = computed(() => whiteboardStore.currentUserColor)

const userInitial = (name) => {
  return name ? name.charAt(0).toUpperCase() : 'U'
}

const formatTime = (isoString) => {
  const date = new Date(isoString)
  return date.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })
}

const copyBoardLink = () => {
  const link = `${window.location.origin}/board/${boardId}`
  navigator.clipboard.writeText(link)
  notificationStore.success('Link Copied!', 'Share this link with others to collaborate', 3000)
}

const getUserFromStorage = () => {
  const storedUser = localStorage.getItem(`whiteboard_user_${boardId}`)
  if (storedUser) {
    const { userId, userName, sessionId, timestamp } = JSON.parse(storedUser)
    const isSessionValid = Date.now() - timestamp < 24 * 60 * 60 * 1000
    if (isSessionValid) {
      return { userId, userName, sessionId }
    }
  }
  return null
}

const updateUserName = () => {
  if (!newUserName.value.trim()) return
  
  const oldName = userDisplayName.value
  userDisplayName.value = newUserName.value.trim()
  newUserName.value = ''
  showNameChange.value = false
  
  // Save to localStorage
  const storedUser = JSON.parse(localStorage.getItem(`whiteboard_user_${boardId}`) || '{}')
  storedUser.userName = userDisplayName.value
  localStorage.setItem(`whiteboard_user_${boardId}`, JSON.stringify(storedUser))
  
  notificationStore.success('Name Updated', `Your name is now ${userDisplayName.value}`)
}

const handleUserNameChanged = (newName) => {
  userDisplayName.value = newName
  // Force update the users list
  if (whiteboardStore.currentBoard?.users) {
    const userIndex = whiteboardStore.currentBoard.users.findIndex(u => u.id === currentUserId.value)
    if (userIndex !== -1) {
      whiteboardStore.currentBoard.users[userIndex].name = newName
    }
  }
}

const saveUserToStorage = (userId, userName, sessionId) => {
  const userData = {
    userId,
    userName,
    sessionId,
    timestamp: Date.now()
  }
  localStorage.setItem(`whiteboard_user_${boardId}`, JSON.stringify(userData))
}

const generateUserName = () => {
  const adjectives = ['Creative', 'Artistic', 'Clever', 'Bright', 'Quick', 'Witty', 'Sharp', 'Smart']
  const nouns = ['Artist', 'Designer', 'Creator', 'Thinker', 'Drafter', 'Sketch', 'Drawer', 'Planner']
  const randomAdj = adjectives[Math.floor(Math.random() * adjectives.length)]
  const randomNoun = nouns[Math.floor(Math.random() * nouns.length)]
  return `${randomAdj} ${randomNoun}`
}

const initializeUser = () => {
  const storedUser = getUserFromStorage()
  if (storedUser) {
    userDisplayName.value = storedUser.userName
    userSessionId.value = storedUser.sessionId
  } else {
    userDisplayName.value = generateUserName()
    userSessionId.value = Date.now().toString(36) + Math.random().toString(36).substr(2)
  }
}

const setupWebSocket = () => {
  const protocol = window.location.protocol === 'https:' ? 'wss:' : 'ws:'
  const host = import.meta.env.VITE_WS_URL 
  
  socket.value = new WebSocket(`${protocol}//${host}/ws/${boardId}`)
  
  socket.value.onopen = () => {
    isConnected.value = true
    console.log('Connected to WebSocket server')
    
    const message = {
      type: 'user_join',
      userId: currentUserId.value,
      userName: userDisplayName.value,
      sessionId: userSessionId.value,
      isReconnect: !!userSessionId.value
    }
    socket.value.send(JSON.stringify(message))
    
    notificationStore.success('Connected!', `You're now on board ${boardId}`)
    
    // Start ping interval
    startPingInterval()
  }
  
  socket.value.onmessage = (event) => {
    try {
      const data = JSON.parse(event.data)
      handleWebSocketMessage(data)
    } catch (error) {
      console.error('Error parsing WebSocket message:', error)
    }
  }
  
  socket.value.onclose = () => {
    isConnected.value = false
    notificationStore.error('Disconnected', 'Lost connection. Reconnecting...')
    setTimeout(setupWebSocket, 3000)
  }
  
  socket.value.onerror = (error) => {
    console.error('WebSocket error:', error)
    notificationStore.error('Connection Error', 'Failed to connect to the server')
  }
}

const handleWebSocketMessage = (data) => {
  switch (data.type) {
    case 'init':
      whiteboardStore.setCurrentUser(data.user_id, data.user_color, data.user_name)
      userDisplayName.value = data.user_name
      userSessionId.value = data.session_id
      saveUserToStorage(data.user_id, data.user_name, data.session_id)
      whiteboardStore.currentBoard.users = data.users || []
      break
    case 'user_joined':
      whiteboardStore.addUser(data.user)
      notificationStore.info('User Joined', `${data.user.name} joined the board`)
      break
    case 'user_left':
      whiteboardStore.removeUser(data.user_id)
      notificationStore.info('User Left', `${data.user_name} left the board`)
      break
    case 'board_cleared':
      notificationStore.info('Board Cleared', `${data.user_name} cleared the board`)

    case 'user_updated': // ADD THIS CASE
      // Update user in the store
      if (whiteboardStore.currentBoard?.users) {
        const userIndex = whiteboardStore.currentBoard.users.findIndex(u => u.id === data.user_id)
        if (userIndex !== -1) {
          whiteboardStore.currentBoard.users[userIndex].name = data.newName
        }
      }
      
      // If it's the current user, update the display name
      if (data.user_id === currentUserId.value) {
        userDisplayName.value = data.newName
      }
      
      notificationStore.info('User Updated', `${data.oldName} changed name to ${data.newName}`)
      break
    default:
      // Pass other messages to FabricWhiteboard
      if (whiteboardRef.value) {
        whiteboardRef.value.handleWebSocketMessage(data)
      }
  }
}

const startPingInterval = () => {
  const interval = setInterval(() => {
    if (socket.value && socket.value.readyState === WebSocket.OPEN) {
      socket.value.send(JSON.stringify({ type: 'ping' }))
    } else {
      clearInterval(interval)
    }
  }, 30000)
}

const updateUsersList = () => {
  // This will be called when FabricWhiteboard emits update-users
  // We can refresh the users list if needed
}

const handleBoardCleared = () => {
  notificationStore.info('Board Cleared', 'You cleared the board')
}

onMounted(() => {
  whiteboardStore.joinBoard(boardId)
  initializeUser()
  
  nextTick(() => {
    setupWebSocket()
  })
  
  // Save to recent boards
  let recent = JSON.parse(localStorage.getItem('recentBoards') || '[]')
  recent = recent.filter(id => id !== boardId)
  recent.unshift(boardId)
  if (recent.length > 5) recent = recent.slice(0, 5)
  localStorage.setItem('recentBoards', JSON.stringify(recent))
})

onUnmounted(() => {
  if (socket.value) {
    socket.value.close()
  }
})
</script>