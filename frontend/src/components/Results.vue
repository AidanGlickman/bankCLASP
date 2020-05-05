<template>
  <div class="Results">
    <h1>Players</h1>
    <b-form inline>
      <label class="sr-only" for="inline-form-input-name">Name</label>
      <input
        id="inline-form-input-name"
        class="mb-2 mr-sm-2 mb-sm-0"
        placeholder="Name"
        v-model="filters.name"
      />
    </b-form>
    <ul>
      <li v-for="player in filteredPlayers" v-bind:key="player.id">
        {{player.name}}:
        <ul>
          <li
            v-for="similar in player.similar"
            v-bind:key="similar"
          >{{similar.name}}: {{similar.similarity}}</li>
        </ul>
      </li>
    </ul>
  </div>
</template>

<script>
import fuzzy from "fuzzy";
import axios from "axios";

export default {
  data: () => {
    return {
      players: [],
      filters: {
        name: ""
      }
    };
  },

  created: function() {
    axios.get("/players.json").then(response => {
      this.players = response.data;
    });
  },

  computed: {
    filteredPlayers() {
      var options = {
        extract: function(el) {
          return el.name;
        }
      };
      return fuzzy.filter(this.filters.name, this.players, options).map(res => {
        return { ...res.original, name: res.string };
      });
    }
  }
};
</script>