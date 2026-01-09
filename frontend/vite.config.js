import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import tailwindcss from '@tailwindcss/vite'
import { fileURLToPath, URL } from 'node:url'

// https://vite.dev/config/
export default defineConfig(({ mode }) => {
  const isProduction = mode === 'production'
  
  return {
    base: isProduction ? '/' : '/',
    plugins: [vue(), tailwindcss()],
    resolve: {
      alias: {
        '@': fileURLToPath(new URL('./src', import.meta.url))
      }
    },
    server: !isProduction ? {
      port: 3000,
      proxy: {
        '/ws': {
          target: 'http://localhost:8000',
          ws: true
        },
        '/api': {
          target: 'http://localhost:8000',
          changeOrigin: true
        }
      }
    } : undefined,
    // Build configuration for production
    build: {
      outDir: 'dist',
      sourcemap: isProduction ? false : true,
      rollupOptions: {
        output: {
          manualChunks: {
            'vue-vendor': ['vue', 'vue-router', 'pinia'],
            'fabric-vendor': ['fabric'],
            'notivue-vendor': ['notivue']
          }
        }
      },
      chunkSizeWarningLimit: 1000,
      emptyOutDir: true
    },
    // Preview server for Render
    preview: {
      port: 3000,
      host: true, // Listen on all network interfaces
      cors: true,
      headers: {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'GET, POST, PUT, DELETE, OPTIONS',
        'Access-Control-Allow-Headers': 'Content-Type, Authorization'
      }
    }
  }
})