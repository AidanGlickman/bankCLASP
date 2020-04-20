<template>
  <div id="app">
    <Topbar/>
  </div>
</template>

<script>
import Topbar from '@/components/Topbar.vue'
export default {
  name: "App",
  components: {
    Topbar,
  },
};
</script>

<style lang="scss">
    #app {
        margin: 0 auto;
        width: 1200px;
    }
</style>
