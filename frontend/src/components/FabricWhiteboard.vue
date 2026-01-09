<template>
  <div class="fabric-whiteboard flex flex-col gap-2 relative w-full h-full bg-gray-900">
    <!-- Floating Toolbar -->
    <div class=" top-4 w-full min-w-full transform  z-30">
      <div class="flex flex-col   w-full md:flex-row md:flex-wrap items-center gap-2 p-3 bg-gray-800/80 backdrop-blur-xl 
                   border border-gray-700/50 shadow-2xl shadow-black/40">
        
        <!-- Drawing Tools -->
        <div class="flex items-center  gap-1 p-1 bg-gray-700/30 rounded-xl">
          <!-- Select Tool -->
          <button @click="selectTool('select')" 
                  :class="[
                    'p-2.5 rounded-lg transition-all duration-200 relative group',
                    activeTool === 'select' 
                      ? 'bg-gradient-to-br from-blue-500/20 to-blue-600/20 border border-blue-500/30 text-blue-300'
                      : 'hover:bg-gray-700/50 border border-transparent text-gray-300'
                  ]"
                  title="Select (V)">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" 
                    d="M4 8V4m0 0h4M4 4l5 5m11-1V4m0 0h-4m4 0l-5 5M4 16v4m0 0h4m-4 0l5-5m11 5v-4m0 4h-4m4 0l-5-5" />
            </svg>
            <div class="absolute -top-1 -right-1 w-2 h-2 rounded-full bg-blue-400 animate-pulse" 
                 v-if="activeTool === 'select'"></div>
          </button>
          
          <!-- Pencil Tool -->
          <button @click="selectTool('pencil')" 
                  :class="[
                    'p-2.5 rounded-lg transition-all duration-200 relative group',
                    activeTool === 'pencil' 
                      ? 'bg-gradient-to-br from-purple-500/20 to-purple-600/20 border border-purple-500/30 text-purple-300'
                      : 'hover:bg-gray-700/50 border border-transparent text-gray-300'
                  ]"
                  title="Pencil (P)">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" 
                    d="M15.232 5.232l3.536 3.536m-2.036-5.036a2.5 2.5 0 113.536 3.536L6.5 21.036H3v-3.572L16.732 3.732z" />
            </svg>
          </button>
          
          <!-- Rectangle Tool -->
          <button @click="selectTool('rectangle')" 
                  :class="[
                    'p-2.5 rounded-lg transition-all duration-200 relative group',
                    activeTool === 'rectangle' 
                      ? 'bg-gradient-to-br from-emerald-500/20 to-emerald-600/20 border border-emerald-500/30 text-emerald-300'
                      : 'hover:bg-gray-700/50 border border-transparent text-gray-300'
                  ]"
                  title="Rectangle (R)">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" 
                    d="M3 5a2 2 0 012-2h14a2 2 0 012 2v14a2 2 0 01-2 2H5a2 2 0 01-2-2V5z" />
            </svg>
          </button>
          
          <!-- Circle Tool -->
          <button @click="selectTool('circle')" 
                  :class="[
                    'p-2.5 rounded-lg transition-all duration-200 relative group',
                    activeTool === 'circle' 
                      ? 'bg-gradient-to-br from-amber-500/20 to-amber-600/20 border border-amber-500/30 text-amber-300'
                      : 'hover:bg-gray-700/50 border border-transparent text-gray-300'
                  ]"
                  title="Circle (C)">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" 
                    d="M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
            </svg>
          </button>
          
          <!-- Text Tool -->
          <button @click="selectTool('text')" 
                  :class="[
                    'p-2.5 rounded-lg transition-all duration-200 relative group',
                    activeTool === 'text' 
                      ? 'bg-gradient-to-br from-cyan-500/20 to-cyan-600/20 border border-cyan-500/30 text-cyan-300'
                      : 'hover:bg-gray-700/50 border border-transparent text-gray-300'
                  ]"
                  title="Text (T)">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" 
                    d="M3 10h18M3 14h18m-9-4v8m-7 0h14a2 2 0 002-2V8a2 2 0 00-2-2H5a2 2 0 00-2 2v8a2 2 0 002 2z" />
            </svg>
          </button>
          
          <!-- Eraser Tool -->
          <button @click="selectTool('eraser')" 
                  :class="[
                    'p-2.5 rounded-lg transition-all duration-200 relative group',
                    activeTool === 'eraser' 
                      ? 'bg-gradient-to-br from-red-500/20 to-red-600/20 border border-red-500/30 text-red-300'
                      : 'hover:bg-gray-700/50 border border-transparent text-gray-300'
                  ]"
                  title="Eraser (E)">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" 
                    d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16" />
            </svg>
          </button>
        </div>
        
        <div class="h-6 w-px bg-gray-600/50 hidden md:block"></div>
        
        <!-- Color Picker & Stroke -->
        <div class="flex  items-center gap-3">
          <!-- Color Palette -->
          <div class="flex flex-row flex-wrap items-center gap-1 p-1 bg-gray-700/30 rounded-xl">
            <button
              v-for="color in colors"
              :key="color"
              @click="setColor(color)"
              :class="[
                'w-7 h-7 rounded-full border-2 transition-all duration-200 hover:scale-110',
                strokeColor === color 
                  ? 'border-white scale-110 ring-2 ring-white/30' 
                  : 'border-gray-600 hover:border-gray-400'
              ]"
              :style="{ backgroundColor: color }"
              :title="color"
            />
          </div>
          
          <div class="flex flex-col-reverse md:flex-row md:gap-2 flex-wrap align-middle" >          
            <!-- Custom Color -->
            <div class="relative  group">
              <input type="color" v-model="strokeColor" @input="setColor(strokeColor)" 
                    class="w-9 h-9 rounded-full cursor-pointer border-2 border-gray-600 hover:border-gray-400
                            transition-all duration-200 hover:scale-110" />
              <div class="absolute -top-8 left-1/2 transform -translate-x-1/2 bg-gray-800 text-white text-xs
                          px-2 py-1 rounded opacity-0 group-hover:opacity-100 transition-opacity duration-200
                          whitespace-nowrap pointer-events-none">
                Custom Color
              </div>
            </div>
            
            <!-- Stroke Width -->
            <div class="flex flex-col items-center gap-1">
              <div class="flex items-center gap-2">
                <div class="w-4 h-4 rounded-full border border-gray-500" 
                    :style="{ backgroundColor: strokeColor }"></div>
                <span class="text-xs text-gray-300 font-medium">{{ strokeWidth }}px</span>
              </div>
              <input type="range" min="1" max="50" v-model="strokeWidth" @input="setStrokeWidth" 
                    class="w-24 accent-blue-500 cursor-pointer" />
            </div>
          </div>
        </div>
        
        <div class="h-6 w-px bg-gray-600/50 hidden md:block"></div>
        
        <!-- Action Buttons -->
        <div class="flex flex-row flex-wrap w-full items-center gap-1">
          <!-- Fill Toggle -->
          <button @click="toggleFill" 
                  :class="[
                    'p-2.5 rounded-lg transition-all duration-200 flex items-center gap-2',
                    fillEnabled 
                      ? 'bg-gradient-to-br from-pink-500/20 to-pink-600/20 border border-pink-500/30 text-pink-300'
                      : 'hover:bg-gray-700/50 border border-transparent text-gray-300'
                  ]"
                  title="Toggle Fill">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" 
                    d="M7 20l4-16m2 16l4-16M6 9h14M4 15h14" />
            </svg>
            <span class="hidden sm:inline text-sm">Fill</span>
          </button>
          
          <!-- Undo/Redo -->
          <button @click="undo" :disabled="!canUndo" 
                  :class="[
                    'p-2.5 rounded-lg transition-all duration-200',
                    canUndo 
                      ? 'hover:bg-gray-700/50 border border-transparent text-gray-300' 
                      : 'opacity-30 cursor-not-allowed text-gray-500'
                  ]"
                  title="Undo (Ctrl+Z)">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" 
                    d="M3 10h10a8 8 0 018 8v2M3 10l6 6m-6-6l6-6" />
            </svg>
          </button>
          
          <button @click="redo" :disabled="!canRedo" 
                  :class="[
                    'p-2.5 rounded-lg transition-all duration-200',
                    canRedo 
                      ? 'hover:bg-gray-700/50 border border-transparent text-gray-300' 
                      : 'opacity-30 cursor-not-allowed text-gray-500'
                  ]"
                  title="Redo (Ctrl+Y)">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" 
                    d="M14 5l7 7m0 0l-7 7m7-7H3" />
            </svg>
          </button>
          
          <!-- Clear -->
          <button @click="clearCanvas" 
                  class="p-2.5 rounded-lg hover:bg-red-500/20 border border-transparent 
                         hover:border-red-500/30 text-gray-300 hover:text-red-300 
                         transition-all duration-200"
                  title="Clear Canvas">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" 
                    d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16" />
            </svg>
          </button>

            <!-- Zoom Controls -->
          <div class="flex w-fit items-center gap-2">
            <div class="flex items-center gap-1">
              <button @click="zoomOut" 
                      class="p-2 rounded-lg hover:bg-gray-700/50 border border-transparent 
                            text-gray-300 transition-all duration-200"
                      title="Zoom Out (-)">
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20 12H4" />
                </svg>
              </button>
              <span class="text-sm font-semibold text-blue-300 bg-gray-800 px-3 py-1 rounded-lg">
                {{ Math.round(zoom * 100) }}%
              </span>
              <button @click="zoomIn" 
                      class="p-2 rounded-lg hover:bg-gray-700/50 border border-transparent 
                            text-gray-300 transition-all duration-200"
                      title="Zoom In (+)">
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" 
                        d="M12 6v6m0 0v6m0-6h6m-6 0H6" />
                </svg>
              </button>
            </div>
            <button @click="resetZoom" 
                    class="px-3 py-1 text-sm bg-gray-700/50 hover:bg-gray-600/50 rounded-lg 
                          border border-gray-600/50 text-gray-300 transition-all duration-200"
                    title="Reset Zoom (1:1)">
              1:1
            </button>
          </div>

        </div>
        
        
        
        
      </div>
    </div>
    
    <!-- Right Side Toolbar 🕯️ -->
    <div v-if="AdditionalFeutures" class="absolute  top-6 right-4 z-30">
      <div class="flex flex-col gap-3">
        <!-- Grid & Snap Toggle -->
        <div class="flex flex-col gap-2 p-3 bg-gray-800/80 backdrop-blur-xl rounded-xl 
                    border border-gray-700/50 shadow-lg">
          <button @click="toggleGrid" 
                  :class="[
                    'flex items-center gap-2 px-3 py-2 rounded-lg transition-all duration-200',
                    showGrid 
                      ? 'bg-gradient-to-r from-blue-500/20 to-blue-600/20 border border-blue-500/30 text-blue-300'
                      : 'hover:bg-gray-700/50 border border-transparent text-gray-300'
                  ]"
                  title="Toggle Grid">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" 
                    d="M4 6a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2H6a2 2 0 01-2-2V6zM14 6a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2V6zM4 16a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2H6a2 2 0 01-2-2v-2zM14 16a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2v-2z" />
            </svg>
            <span class="text-sm">Grid</span>
          </button>
          
          <button @click="toggleSnap" 
                  :class="[
                    'flex items-center gap-2 px-3 py-2 rounded-lg transition-all duration-200',
                    snapToGrid 
                      ? 'bg-gradient-to-r from-emerald-500/20 to-emerald-600/20 border border-emerald-500/30 text-emerald-300'
                      : 'hover:bg-gray-700/50 border border-transparent text-gray-300'
                  ]"
                  title="Toggle Snap to Grid">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" 
                    d="M10 20l4-16m4 4l4 4-4 4M6 16l-4-4 4-4" />
            </svg>
            <span class="text-sm">Snap</span>
          </button>
        </div>
        
        <!-- Export/Import -->
        <div class="flex flex-col gap-2 p-3 bg-gray-800/80 backdrop-blur-xl rounded-xl 
                    border border-gray-700/50 shadow-lg">
          <button @click="exportJSON" 
                  class="flex items-center gap-2 px-3 py-2 rounded-lg hover:bg-gray-700/50 
                         border border-transparent text-gray-300 transition-all duration-200"
                  title="Export as JSON">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" 
                    d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4" />
            </svg>
            <span class="text-sm">Export</span>
          </button>
          
          <button @click="exportImage" 
                  class="flex items-center gap-2 px-3 py-2 rounded-lg hover:bg-gray-700/50 
                         border border-transparent text-gray-300 transition-all duration-200"
                  title="Export as Image">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" 
                    d="M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z" />
            </svg>
            <span class="text-sm">Image</span>
          </button>
          
          <button @click="importJSON" 
                  class="flex items-center gap-2 px-3 py-2 rounded-lg hover:bg-gray-700/50 
                         border border-transparent text-gray-300 transition-all duration-200"
                  title="Import JSON">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" 
                    d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M9 19l3 3m0 0l3-3m-3 3V10" />
            </svg>
            <span class="text-sm">Import</span>
          </button>
        </div>
        
        <!-- User Name -->
        <div class="p-3 bg-gray-800/80 backdrop-blur-xl rounded-xl border border-gray-700/50 shadow-lg">
          <button @click="showNameChange = true" 
                  class="flex items-center gap-2 px-3 py-2 rounded-lg hover:bg-blue-500/20 
                         border border-transparent hover:border-blue-500/30 text-gray-300 
                         transition-all duration-200 w-full">
            <div class="w-8 h-8 rounded-full flex items-center justify-center text-sm font-bold"
                 :style="{ backgroundColor: props.userColor }">
              {{ userInitial(props.userName) }}
            </div>
            <div class="flex-1 text-left">
              <p class="text-sm font-medium truncate max-w-[120px]">{{ props.userName || 'User' }}</p>
              <p class="text-xs text-gray-400">Click to change</p>
            </div>
          </button>
        </div>
      </div>
    </div>
    
    <!-- Bottom Bar 🕯️ -->
    <div v-if="AdditionalFeutures" class="fixed bottom-4  left-1/2 transform -translate-x-1/2 z-30">
      <div class="flex items-center gap-2 p-3 bg-gray-800/80 backdrop-blur-xl rounded-xl 
                  border border-gray-700/50 shadow-lg">
        <!-- History Timeline -->
        <button @click="toggleHistory" 
                class="flex items-center gap-2 px-4 py-2 rounded-lg hover:bg-gray-700/50 
                       border border-transparent text-gray-300 transition-all duration-200"
                :class="{ 'bg-purple-500/20 border-purple-500/30 text-purple-300': showHistory }">
          <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" 
                  d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" />
          </svg>
          <span class="hidden sm:inline">History</span>
        </button>
        
        <!-- Stickers -->
        <button @click="toggleStickers" 
                class="flex items-center gap-2 px-4 py-2 rounded-lg hover:bg-gray-700/50 
                       border border-transparent text-gray-300 transition-all duration-200"
                :class="{ 'bg-pink-500/20 border-pink-500/30 text-pink-300': showStickers }">
          <span class="text-lg">😊</span>
          <span class="hidden sm:inline">Stickers</span>
        </button>
        
        <!-- Right Click Toggle -->
        <label class="flex items-center gap-2 px-4 py-2 rounded-lg hover:bg-gray-700/50 
                      border border-transparent text-gray-300 transition-all duration-200 cursor-pointer">
          <input type="checkbox" v-model="rightClickEnabled" 
                 class="w-4 h-4 accent-blue-500 rounded" />
          <span class="text-sm">Right-click</span>
        </label>
        
        <!-- Fill Color Picker (if enabled) -->
        <div v-if="fillEnabled" class="flex items-center gap-2">
          <span class="text-sm text-gray-400">Fill:</span>
          <input type="color" v-model="fillColor" @input="setFillColor" 
                 class="w-6 h-6 rounded cursor-pointer border border-gray-600" />
        </div>
      </div>
    </div>
    
    <!-- Canvas Container -->
    <div class="canvas-container absolute inset-0 z-10" ref="canvasContainer">
      <canvas ref="canvas" class="absolute inset-0"></canvas>
      
      <!-- Live Cursors -->
      <div class="cursors-overlay absolute inset-0 pointer-events-none z-20">
        <div
          v-for="(cursor, userId) in liveCursors"
          :key="userId"
          class="cursor absolute transform -translate-x-1/2 -translate-y-1/2 transition-all duration-100"
          :style="{
            left: cursor.x + 'px',
            top: cursor.y + 'px',
          }"
        >
          <div class="relative">
            <div class="absolute -top-6 left-1/2 transform -translate-x-1/2 bg-gray-900/90 
                        text-white text-xs px-2 py-1 rounded-lg whitespace-nowrap 
                        border border-gray-700/50 backdrop-blur-sm">
              {{ cursor.name }}
            </div>
            <div class="w-6 h-6 rounded-full border-2"
                 :style="{ borderColor: cursor.color }">
              <div class="w-3 h-3 rounded-full m-1.5" 
                   :style="{ backgroundColor: cursor.color }"></div>
            </div>
          </div>
        </div>
      </div>
    </div>
    
    <!-- Text Input Modal -->
    <div v-if="textInputActive" class="fixed inset-0  bg-black/60 backdrop-blur-sm flex items-center justify-center z-50 p-4">
      <div class="bg-gradient-to-br from-gray-800 to-gray-900 p-6 rounded-2xl shadow-2xl 
                  border border-gray-700/50 max-w-md w-full">
        <h3 class="text-xl font-bold text-white mb-4">Add Text</h3>
        <input
          v-model="textInput"
          @keyup.enter="addText"
          @keyup.esc="cancelText"
          placeholder="Enter text here..."
          ref="textInputField"
          autofocus
          class="w-full px-4 py-3 bg-gray-700/50 border border-gray-600/50 rounded-xl 
                 focus:border-blue-500/50 focus:ring-2 focus:ring-blue-500/30 
                 focus:outline-none text-white placeholder-gray-400 mb-4"
        />
        <div class="flex justify-end gap-3">
          <button @click="cancelText" 
                  class="px-5 py-2 bg-gray-700/50 hover:bg-gray-600/50 border border-gray-600/50 
                         rounded-xl font-medium transition-all duration-200">
            Cancel
          </button>
          <button @click="addText" 
                  class="px-5 py-2 bg-gradient-to-r from-blue-600 to-blue-700 hover:from-blue-500 hover:to-blue-600 
                         rounded-xl font-medium shadow-lg shadow-blue-500/20 hover:shadow-blue-500/30
                         border border-blue-500/30 transition-all duration-200">
            Add Text
          </button>
        </div>
      </div>
    </div>
    
    <!-- Name Change Modal -->
    <div v-if="showNameChange" class="fixed inset-0 bg-black/60 backdrop-blur-sm flex items-center justify-center z-50 p-4">
      <div class="bg-gradient-to-br from-gray-800 to-gray-900 p-6 rounded-2xl shadow-2xl 
                  border border-gray-700/50 max-w-md w-full">
        <h3 class="text-xl font-bold text-white mb-4">Change Your Name</h3>
        <input
          v-model="newUserName"
          @keyup.enter="updateUserName"
          placeholder="Enter your display name..."
          class="w-full px-4 py-3 bg-gray-700/50 border border-gray-600/50 rounded-xl 
                 focus:border-blue-500/50 focus:ring-2 focus:ring-blue-500/30 
                 focus:outline-none text-white placeholder-gray-400 mb-4"
          autofocus
        />
        <div class="flex justify-end gap-3">
          <button @click="showNameChange = false" 
                  class="px-5 py-2 bg-gray-700/50 hover:bg-gray-600/50 border border-gray-600/50 
                         rounded-xl font-medium transition-all duration-200">
            Cancel
          </button>
          <button @click="updateUserName" 
                  class="px-5 py-2 bg-gradient-to-r from-blue-600 to-blue-700 hover:from-blue-500 hover:to-blue-600 
                         rounded-xl font-medium shadow-lg shadow-blue-500/20 hover:shadow-blue-500/30
                         border border-blue-500/30 transition-all duration-200">
            Update Name
          </button>
        </div>
      </div>
    </div>
    
    <!-- Stickers Panel -->
    <div v-if="showStickers" 
         class="absolute bottom-20 left-1/2 transform -translate-x-1/2 z-40
                bg-gray-800/95 backdrop-blur-xl rounded-2xl border border-gray-700/50 
                shadow-2xl p-4 max-w-md w-full mx-4">
      <h3 class="text-lg font-bold text-white mb-4 flex items-center gap-2">
        <span class="text-lg">🎨</span> Stickers & Emojis
      </h3>
      <div class="grid grid-cols-6 sm:grid-cols-8 gap-2 max-h-60 overflow-y-auto p-2">
        <button
          v-for="sticker in stickers"
          :key="sticker.emoji"
          @click="addSticker(sticker)"
          class="sticker-btn text-2xl hover:scale-125 transition-transform duration-200 
                 hover:bg-gray-700/50 p-2 rounded-lg"
          :title="sticker.name"
        >
          {{ sticker.emoji }}
        </button>
      </div>
    </div>
    
    <!-- History Timeline -->
    <div v-if="showHistory" 
         class="absolute bottom-20 right-4 z-40 bg-gray-800/95 backdrop-blur-xl 
                rounded-2xl border border-gray-700/50 shadow-2xl p-4 w-80">
      <h3 class="text-lg font-bold text-white mb-4 flex items-center gap-2">
        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" 
                d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" />
        </svg>
        History Timeline
      </h3>
      <div class="space-y-2 max-h-60 overflow-y-auto">
        <div
          v-for="(action, index) in history"
          :key="index"
          @click="restoreHistory(index)"
          :class="[
            'history-item p-3 rounded-lg border transition-all duration-200 cursor-pointer',
            historyIndex === index 
              ? 'bg-gradient-to-r from-purple-500/20 to-purple-600/20 border-purple-500/30 text-purple-300'
              : 'hover:bg-gray-700/50 border-gray-600/30 text-gray-300'
          ]"
        >
          <div class="flex items-center justify-between">
            <span class="font-medium capitalize">{{ action.type }}</span>
            <span class="text-xs text-gray-400">
              {{ new Date(action.timestamp).toLocaleTimeString([], {hour: '2-digit', minute:'2-digit'}) }}
            </span>
          </div>
          <div class="text-xs text-gray-400 mt-1">
            {{ action.user || 'Unknown' }}
          </div>
        </div>
      </div>
    </div>

    <!-- Mobile Floating Action Button -->
    <div class=" fixed bottom-6 group right-6 z-40">
      <button @click="showAdditionalFeutures"
              class="w-12 h-12 rounded-full cursor-pointer bg-gradient-to-r from-blue-600 to-blue-700 
                      shadow-lg shadow-blue-500/30 border border-blue-500/30 flex items-center justify-center">
        <svg class="w-6 h-6 group-hover:animate-spin text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6v6m0 0v6m0-6h6m-6 0H6" />
        </svg>
      </button>
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
const AdditionalFeutures = ref(false)
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
const userInitial = (name) => {
  return name ? name.charAt(0).toUpperCase() : 'U'
}

const toggleHistory = () => {
  showHistory.value = !showHistory.value
}

const toggleStickers = () => {
  showStickers.value = !showStickers.value
}

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

const showAdditionalFeutures =() =>{
  // console.log('clicked')
  AdditionalFeutures.value = !AdditionalFeutures.value
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
    case 'text':
      fabricCanvas.defaultCursor = 'text'
      fabricCanvas.selection = false  // Disable selection for text tool
      
      // Setup text tool click handler
      setupTextTool()
      break
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
  // console.log('📨 Received WebSocket:', data.type, data)
  
  switch (data.type) {
    case 'object_added':
      // console.log('🟢 Adding remote object:', data.object?.type, 'from:', data.object?.userName)
      addRemoteObject(data.object)
      break
      
    case 'object_modified':
      // console.log('🟡 Modifying remote object:', data.object_id,data.object)
    //   data.object.id = data.object_id
      modifyRemoteObject(data.object,data.object_id)
      break
      
    case 'clear_board':
      // console.log('🗑️ Board cleared by:', data.user_name)
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
      // console.log('🔴 Removing remote object:', data.object_id)
      removeRemoteObject(data.object_id)
      break
    case 'cursor_moved':
      // console.log('🎯 CURSOR MOVED received:', {
      //   user: data.user_name,
      //   userId: data.user_id,
      //   position: data.position,
      //   color: data.user_color
      // })
      updateLiveCursor(data)
      
      break
      
    default:
      // console.log('⚪ Unknown message type:', data.type)
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
    // console.log('🖱️ Container mouse move detected', e)
    
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
    
    // console.log('📤 Sending cursor move from container:', cursorData)
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