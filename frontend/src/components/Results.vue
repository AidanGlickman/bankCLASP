<template>
  <div class="Results">
    <h1>Players</h1>
    <form v-on:submit="onSubmit" inline>
      <label class="sr-only" for="inline-form-input-name">Name</label>
      <input
        id="inline-form-input-name"
        class="mb-2 mr-sm-2 mb-sm-0"
        placeholder="Name"
        v-model="filters.name"
      />
      <Dropdown
      :options="[{ id: 1, name: 'Option 1'}, { id: 2, name: 'Option 2'}]"
      v-on:selected="validateSelection"
      v-on:filter="getDropdownValues"
      :disabled="false"
      name="zipcode"
      :maxItem="10"
      placeholder="Please select an option">
      </Dropdown>
    </form>
    
    <!-- <ul>
      <li v-for="player in filteredPlayers" v-bind:key="player.id">
        {{player.name}}:
        <ul>
          <li
            v-for="similar in player.similar"
            v-bind:key="similar"
          >{{similar.name}}: {{similar.similarity}}</li>
        </ul>
      </li>
    </ul> -->
  </div>
</template>

<script>
import fuzzy from "fuzzy";
import axios from "axios";

export default {
  name: "results",
  data: () => {
    return {
      players: [],
      filters: {
        name: ""
      }
    };
  },
  methods: {
    onSubmit: function() {
      this.$router.push("/player/" + this.filteredPlayers[0].id)
    }
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