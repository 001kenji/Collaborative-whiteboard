<template>
  <div class="min-h-screen flex items-center justify-center bg-gradient-to-br from-blue-50 to-indigo-100">
    <!-- Server Loading Card -->
    <div 
      v-if="showServerLoading"
      class="fixed top-4 left-1/2 transform -translate-x-1/2 z-50 max-w-md w-full mx-4"
    >
      <div class="bg-gradient-to-r from-yellow-500 to-orange-500 text-white rounded-xl shadow-xl p-6 animate-fade-in">
        <div class="flex items-center justify-between mb-4">
          <div class="flex items-center">
            <svg class="w-6 h-6 mr-3 animate-spin" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15" />
            </svg>
            <h3 class="text-lg font-semibold">Server is Starting Up</h3>
          </div>
          <span class="text-sm font-medium bg-white/20 px-3 py-1 rounded-full">
            {{ elapsedTime }}s
          </span>
        </div>
        
        <p class="text-white/90 mb-4">
          Your backend server is waking up. This usually takes about 2 minutes on Render's free tier.
          Please wait while we establish the connection...
        </p>
        
        <div class="space-y-3">
          <div class="flex items-center text-sm">
            <div class="w-8 h-8 rounded-full bg-white/20 flex items-center justify-center mr-3">
              <svg v-if="serverStatus === 'checking'" class="w-4 h-4 animate-pulse" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" />
              </svg>
              <svg v-else-if="serverStatus === 'down'" class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
              </svg>
              <svg v-else class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
              </svg>
            </div>
            <span>Server Status: </span>
            <span class="ml-2 font-medium">
              {{ serverStatusText }}
            </span>
          </div>
          
          <div class="w-full bg-white/20 rounded-full h-2">
            <div 
              class="bg-gradient-to-r from-green-400 to-blue-400 h-2 rounded-full transition-all duration-500"
              :style="{ width: progressPercentage + '%' }"
            ></div>
          </div>
          
          <div class="flex justify-end hidd text-xs">
            
            <span>{{ Math.round(progressPercentage) }}%</span>
          </div>
        </div>
        
        <button
          v-if="serverStatus === 'up'"
          @click="dismissLoading"
          class="mt-4 w-full bg-white text-orange-600 font-semibold py-2 px-4 rounded-lg hover:bg-gray-100 transition"
        >
          Got it! Let's continue →
        </button>
      </div>
    </div>

    <!-- Main Content -->
    <div class="bg-white rounded-2xl shadow-xl p-8 max-w-md w-full mx-4">
      <div class="text-center mb-8">
        <h1 class="text-4xl font-bold text-gray-800 mb-2">🎨 Collaborative Whiteboard</h1>
        <p class="text-gray-600">Draw and collaborate in real-time with your team</p>
        
        <!-- Server Status Indicator -->
        <div v-if="!showServerLoading && serverChecked" class="mt-4 inline-flex items-center px-3 py-1 rounded-full text-sm"
          :class="{
            'bg-green-100 text-green-800': serverStatus === 'up',
            'bg-yellow-100 text-yellow-800': serverStatus === 'checking',
            'bg-red-100 text-red-800': serverStatus === 'down'
          }"
        >
          <span class="w-2 h-2 rounded-full mr-2"
            :class="{
              'bg-green-500 animate-pulse': serverStatus === 'up',
              'bg-yellow-500': serverStatus === 'checking',
              'bg-red-500': serverStatus === 'down'
            }"
          ></span>
          {{ serverStatusText }}
        </div>
      </div>
      
      <div class="space-y-6">
        <div class="bg-blue-50 p-6 rounded-lg border border-blue-100">
          <h2 class="text-xl font-semibold text-gray-800 mb-4">Create New Board</h2>
          <p class="text-gray-600 mb-4">Start a new collaborative whiteboard session</p>
          <button 
            @click="createBoard"
            :disabled="serverStatus !== 'up'"
            class="w-full bg-gradient-to-r from-blue-500 to-indigo-600 text-white font-semibold py-3 px-4 rounded-lg hover:from-blue-600 hover:to-indigo-700 transition-all duration-200 transform hover:-translate-y-0.5 active:translate-y-0 disabled:opacity-50 disabled:cursor-not-allowed disabled:transform-none"
          >
            <template v-if="serverStatus === 'up'">
              Create New Board
            </template>
            <template v-else>
              <span class="flex items-center justify-center">
                <svg class="w-4 h-4 mr-2 animate-spin" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15" />
                </svg>
                Waiting for server...
              </span>
            </template>
          </button>
        </div>
        
        <div class="relative">
          <div class="absolute inset-0 flex items-center">
            <div class="w-full border-t border-gray-300"></div>
          </div>
          <div class="relative flex justify-center text-sm">
            <span class="px-2 bg-white text-gray-500">or join existing board</span>
          </div>
        </div>
        
        <div>
          <label for="boardId" class="block text-sm font-medium text-gray-700 mb-2">Enter Board ID</label>
          <div class="flex gap-2">
            <input
              id="boardId"
              v-model="boardId"
              type="text"
              placeholder="Paste board ID here"
              :disabled="serverStatus !== 'up'"
              class="flex-1 px-4 py-3 border border-gray-300 text-black rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent outline-none transition disabled:opacity-50 disabled:cursor-not-allowed"
            />
            <button
              @click="joinBoard"
              :disabled="!boardId.trim() || serverStatus !== 'up'"
              class="px-6 py-3 bg-green-500 text-white font-semibold rounded-lg hover:bg-green-600 transition disabled:opacity-50 disabled:cursor-not-allowed"
            >
              Join
            </button>
          </div>
        </div>
        
        <div v-if="recentBoards.length > 0" class="hidden mt-8">
          <h3 class="text-lg font-semibold text-gray-800 mb-3">Recent Boards</h3>
          <div class="space-y-2">
            <div
              v-for="board in recentBoards"
              :key="board"
              @click="joinRecentBoard(board)"
              :class="[
                'flex items-center justify-between p-3 rounded-lg transition cursor-pointer',
                serverStatus === 'up' 
                  ? 'bg-gray-50 hover:bg-gray-100' 
                  : 'bg-gray-100 opacity-50 cursor-not-allowed'
              ]"
            >
              <span class="text-gray-700 font-medium">{{ board }}</span>
              <span class="text-blue-500 hover:text-blue-600">Join →</span>
            </div>
          </div>
        </div>
      </div>
      
      <div class="mt-8 text-center text-sm text-gray-500">
        <p>No login required • Real-time collaboration • End-to-end encrypted</p>
      </div>
    </div>

    <!-- Audio element for notification sound -->
    <audio ref="notificationSound" preload="auto">
      <source src="https://assets.mixkit.co/sfx/preview/mixkit-correct-answer-tone-2870.mp3" type="audio/mpeg">
      <source src="https://assets.mixkit.co/sfx/preview/mixkit-correct-answer-tone-2870.wav" type="audio/wav">
    </audio>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted, computed } from 'vue'
import { useRouter } from 'vue-router'
import { useWhiteboardStore } from '@/stores/whiteboard'
import { push } from 'notivue'

const router = useRouter()
const whiteboardStore = useWhiteboardStore()
const boardId = ref('')
const recentBoards = ref([])

// Server health check variables
const showServerLoading = ref(false)
const serverStatus = ref('checking') // 'checking', 'up', 'down'
const checkAttempts = ref(0)
const maxAttempts = ref(40) // 40 attempts * 3 seconds = 120 seconds (2 minutes)
const startTime = ref(null)
const elapsedTime = ref(0)
const checkInterval = ref(null)
const serverChecked = ref(false)
const notificationSound = ref(null)

// Backend URL - update this to your Render backend URL
const backendUrl = import.meta.env.VITE_BACKEND_URL 

// Computed properties
const serverStatusText = computed(() => {
  switch (serverStatus.value) {
    case 'up': return 'Server is ready ✓'
    case 'checking': return 'Checking server...'
    case 'down': return 'Server is starting up...'
    default: return 'Unknown status'
  }
})

const progressPercentage = computed(() => {
  if (serverStatus.value === 'up') return 100
  return Math.min((checkAttempts.value / maxAttempts.value) * 100, 95)
})

// Server health check function
const checkServerHealth = async () => {
  if (checkAttempts.value >= maxAttempts.value) {
    // Maximum attempts reached
    clearInterval(checkInterval.value)
    serverStatus.value = 'down'
    push.error({
      title: 'Server Timeout',
      message: 'The server is taking longer than expected. Please try again in a moment.',
      duration: 5000
    })
    return
  }

  checkAttempts.value++
  elapsedTime.value = Math.floor((Date.now() - startTime.value) / 1000)

  try {
    const response = await fetch(`${backendUrl}/`, {
      method: 'GET',
      headers: {
        'Accept': 'application/json',
      },
      mode: 'cors',
      cache: 'no-cache'
    })

    if (response.ok) {
      const data = await response.json()
      
      if (data.message === "Whiteboard API is running") {
        // Server is up!
        clearInterval(checkInterval.value)
        serverStatus.value = 'up'
        serverChecked.value = true
        
        // Play notification sound
        if (notificationSound.value) {
          try {
            notificationSound.value.currentTime = 0
            await notificationSound.value.play()
          } catch (error) {
            console.log('Could not play notification sound:', error)
          }
        }
        
        // Show success notification
        push.success({
          title: 'Server is Ready!',
          message: 'The whiteboard server is now online and ready to use.',
          duration: 4000
        })
        
        // Auto-dismiss loading card after 4 seconds
        setTimeout(() => {
          showServerLoading.value = false
        }, 4000)
      } else {
        throw new Error('Invalid response from server')
      }
    } else {
      throw new Error(`HTTP ${response.status}`)
    }
  } catch (error) {
    console.log(`Server check attempt ${checkAttempts.value} failed:`, error.message)
    
    // Update status text based on attempts
    if (checkAttempts.value > maxAttempts.value * 0.5) {
      serverStatus.value = 'down'
    }
  }
}

// Start server health monitoring
const startServerHealthCheck = () => {
  startTime.value = Date.now()
  showServerLoading.value = true
  serverStatus.value = 'checking'
  checkAttempts.value = 0
  
  // Check immediately
  checkServerHealth()
  
  // Then check every 3 seconds
  checkInterval.value = setInterval(checkServerHealth, 3000)
  
  // Update elapsed time every second
  const timeInterval = setInterval(() => {
    if (serverStatus.value === 'up') {
      clearInterval(timeInterval)
      return
    }
    elapsedTime.value = Math.floor((Date.now() - startTime.value) / 1000)
  }, 1000)
}

// Dismiss loading card manually
const dismissLoading = () => {
  showServerLoading.value = false
  if (checkInterval.value) {
    clearInterval(checkInterval.value)
  }
}

// Board creation and joining functions
const createBoard = () => {
  if (serverStatus.value !== 'up') {
    push.warning({
      title: 'Server Not Ready',
      message: 'Please wait for the server to start up completely',
      duration: 3000
    })
    return
  }
  
  const newBoardId = whiteboardStore.createBoard()
  push.success({
    title: 'Board Created!',
    message: 'Share the link with your team to start collaborating',
    duration: 4000
  })
  router.push(`/board/${newBoardId}`)
}

const joinBoard = () => {
  if (serverStatus.value !== 'up') {
    push.warning({
      title: 'Server Not Ready',
      message: 'Please wait for the server to start up completely',
      duration: 3000
    })
    return
  }
  
  if (boardId.value.trim()) {
    whiteboardStore.joinBoard(boardId.value.trim())
    push.success({
      title: 'Joining Board',
      message: 'Connecting to the whiteboard...',
      duration: 3000
    })
    router.push(`/board/${boardId.value.trim()}`)
  }
}

const joinRecentBoard = (id) => {
  if (serverStatus.value !== 'up') {
    push.warning({
      title: 'Server Not Ready',
      message: 'Please wait for the server to start up completely',
      duration: 3000
    })
    return
  }
  
  boardId.value = id
  joinBoard()
}

onMounted(() => {
  // Load recent boards from localStorage
  const saved = localStorage.getItem('recentBoards')
  if (saved) {
    recentBoards.value = JSON.parse(saved)
  }
  
  // Start server health check
  startServerHealthCheck()
})

onUnmounted(() => {
  // Clean up intervals
  if (checkInterval.value) {
    clearInterval(checkInterval.value)
  }
})
</script>

<style scoped>
.animate-fade-in {
  animation: fadeIn 0.5s ease-out;
}

@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translate(-50%, -20px);
  }
  to {
    opacity: 1;
    transform: translate(-50%, 0);
  }
}

@keyframes spin {
  from {
    transform: rotate(0deg);
  }
  to {
    transform: rotate(360deg);
  }
}

.animate-spin {
  animation: spin 1s linear infinite;
}
</style>