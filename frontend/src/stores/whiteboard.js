import { defineStore } from 'pinia'
import { ref, computed } from 'vue'

export const useWhiteboardStore = defineStore('whiteboard', () => {
  const boards = ref({})
  const currentBoardId = ref(null)
  const currentUserId = ref(null)
  const currentUserColor = ref(null)
  const currentUserName = ref(null)
  
  const currentBoard = computed(() => {
    return boards.value[currentBoardId.value]
  })
  
  const createBoard = () => {
    const boardId = generateBoardId()
    boards.value[boardId] = {
      id: boardId,
      elements: [],
      users: [],
      cursors: {}
    }
    currentBoardId.value = boardId
    return boardId
  }
  
  const joinBoard = (boardId) => {
    if (!boards.value[boardId]) {
      boards.value[boardId] = {
        id: boardId,
        elements: [],
        users: [],
        cursors: {}
      }
    }
    currentBoardId.value = boardId
  }
  
  const generateBoardId = () => {
    return Math.random().toString(36).substring(2, 15)
  }
  
  const setCurrentUser = (userId, color, name = null) => {
    currentUserId.value = userId
    currentUserColor.value = color
    if (name) {
      currentUserName.value = name
    }
  }
  
  const addElement = (element) => {
    if (currentBoard.value) {
      currentBoard.value.elements.push(element)
    }
  }
  
  const removeElement = (elementId) => {
    if (currentBoard.value) {
      currentBoard.value.elements = currentBoard.value.elements.filter(
        el => el.id !== elementId
      )
    }
  }
  
  const clearBoard = () => {
    if (currentBoard.value) {
      currentBoard.value.elements = []
    }
  }
  
  const addUser = (user) => {
    if (currentBoard.value) {
      const existingIndex = currentBoard.value.users.findIndex(u => u.id === user.id)
      if (existingIndex === -1) {
        currentBoard.value.users.push(user)
      } else {
        // Update existing user
        currentBoard.value.users[existingIndex] = user
      }
    }
  }
  
  const removeUser = (userId) => {
    if (currentBoard.value) {
      currentBoard.value.users = currentBoard.value.users.filter(
        user => user.id !== userId
      )
      delete currentBoard.value.cursors[userId]
    }
  }
  
  const updateCursor = (userId, position) => {
    if (currentBoard.value) {
      currentBoard.value.cursors[userId] = {
        ...position,
        updatedAt: Date.now()
      }
    }
  }
  
  const cleanupOldCursors = () => {
    if (currentBoard.value) {
      const now = Date.now()
      Object.keys(currentBoard.value.cursors).forEach(userId => {
        if (now - currentBoard.value.cursors[userId].updatedAt > 5000) {
          delete currentBoard.value.cursors[userId]
        }
      })
    }
  }
  
  return {
    boards,
    currentBoardId,
    currentUserId,
    currentUserColor,
    currentUserName,
    currentBoard,
    createBoard,
    joinBoard,
    setCurrentUser,
    addElement,
    removeElement,
    clearBoard,
    addUser,
    removeUser,
    updateCursor,
    cleanupOldCursors
  }
})