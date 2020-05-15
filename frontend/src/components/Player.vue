<template>
    <div>
        <h5 class="center padding-64"><span class="tag wide"><b>SEARCH RESULTS</b></span></h5>
        <a><i>Player Name:</i> {{this.player.name}} (id: {{this.player.id}})</a>
        <p><i><br>Most similar players:</i></p>

        <table width=100%>
            <tr>
                <th>Player Name</th>
                <th>Similarity Score</th> 
            </tr>
            <tr>
                <td>{{this.player.similar[0].name}}</td>
                <td>{{this.player.similar[0].similarity}}</td>
            </tr>
            <tr>
                <td>{{this.player.similar[1].name}}</td>
                <td>{{this.player.similar[1].similarity}}</td>
            </tr>
            <tr>
                <td>{{this.player.similar[2].name}}</td>
                <td>{{this.player.similar[2].similarity}}</td>
            </tr>
            <tr>
                <td>{{this.player.similar[3].name}}</td>
                <td>{{this.player.similar[3].similarity}}</td>
            </tr>
            <tr>
                <td>{{this.player.similar[4].name}}</td>
                <td>{{this.player.similar[4].similarity}}</td>
            </tr>
            </table>
    </div>
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