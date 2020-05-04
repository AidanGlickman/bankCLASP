<template>
  <div id="app">
    <Topbar />
    <router-view />
  </div>
</template>

<script>
import Topbar from "@/components/Topbar.vue";

export default {
  name: "App",
  data() {
    return {};
  },
  components: {
    Topbar,
  },
};
</script>

<style lang="scss">
#app {
  margin: 0 auto;
  width: 1200px;
  font-family: "Courier New", Courier, monospace;
  font-size: 25px;
}
</style>
