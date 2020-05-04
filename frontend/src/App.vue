<template>
  <div id="app">
    <Topbar />
    <HomepageContent />
    <Results />
  </div>
</template>

<script>
import Topbar from "@/components/Topbar.vue";
import HomepageContent from "@/components/HomepageContent.vue";
import Results from "@/components/Results.vue";

export default {
  name: "App",
  data() {
    return {};
  },
  components: {
    Topbar,
    HomepageContent,
    Results
  }
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
