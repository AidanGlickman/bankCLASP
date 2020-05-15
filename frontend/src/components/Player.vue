<template>
    <div>{{this.player}}</div>
</template>

<script>
import axios from "axios"
export default {
    
    name: "player",
    data: function(){
        return {
            player: ''
        }
    },
    created: function() {
        var pid = this.$route.params.id
            axios.get("/players.json").then(response => {
      var players = response.data;
      this.player = players.filter(function(data){return data.id == pid})[0]
    });
    }
};
</script>