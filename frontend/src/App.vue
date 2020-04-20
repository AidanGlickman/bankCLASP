<template>
  <div id="app">
    <Topbar/>
    <HomepageContent/>
  </div>
</template>

<script>
import Topbar from '@/components/Topbar.vue'
import HomepageContent from '@/components/HomepageContent.vue'

export default {
  name: "App",
  components: {
    Topbar,
    HomepageContent,
  },
};
</script>

<style lang="scss">
    #app {
        margin: 0 auto;
        width: 1200px;
    }
</style>
