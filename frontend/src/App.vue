<template>
  <div class="min-h-screen bg-gray-50">
    <router-view />
      <Notivue v-slot="item">
      <Notification :item="item" />
    </Notivue>
  </div>
</template>

<script setup>
import { Notivue, Notification } from 'notivue'
</script>