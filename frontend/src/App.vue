<template>
  <div id="app">
    <Topbar/>
    <HomepageContent/>
    <ResultsBox/>
  </div>
</template>

<script>
import Topbar from '@/components/Topbar.vue'
import HomepageContent from '@/components/HomepageContent.vue'
import ResultsBox from '@/components/ResultsBox.vue'
import json from '@/json/players.json'

export default {
  name: "App",
  data(){
    return{
      myJson: json
    }
  },
  components: {
    Topbar,
    HomepageContent,
    ResultsBox
  },
};
</script>

<style lang="scss">
    #app {
        margin: 0 auto;
        width: 1200px;
        font-family:'Courier New', Courier, monospace;
        font-size:25px;
    }
</style>
