<template>
  <div class="Results">
    <h1>Players</h1>
    <b-form inline>
      <label class="sr-only" for="inline-form-input-name">Name</label>
      <b-input
        id="inline-form-input-name"
        class="mb-2 mr-sm-2 mb-sm-0"
        placeholder="Name"
        v-model="filters.name"
      ></b-input>
    </b-form>
    <ul>
      <li v-for="player in filteredPlayers" v-bind:key="Name">
        <nuxt-link
          :to="'/user/' + student.id"
          v-html="student.name"
        ></nuxt-link>
      </li>
    </ul>
  </div>
</template>

<script>
    import fuzzy from "fuzzy";
    import axios from 'axios';

    export default {
    data: () => {
        return {
        students: [],
        filters: {
            name: ""
        }
        };
    },
    async asyncData(context) {
        const { users } = await getData(context);
        const players = Object.keys(users)
        .map(id => ({ ...users[id], id }))
        .filter(user => user.year)
        .sort((a, b) => {
            if (a.name > b.name) return 1;
            if (a.name < b.name) return -1;
            return 0;
        });
        return {
        players
        };
    },

    async getData(context) {
        const host = (typeof window !== "undefined" && window.location.host) || (process.server && context.req.headers.host);
        const protocol = host.includes("local") ? "http" : "https";
        const { data } = await axios.get(`${protocol}://${host}/data/1920T2.json`);
        return data;
    },

    computed: {
        filteredPlayers() {
        var options = {
            pre: "<strong>",
            post: "</strong>",
            extract: function(el) {
            return el.name;
            }
        };
        return fuzzy
            .filter(this.filters.name, this.players, options)
            .map(res => {
            return { ...res.original, name: res.string };
            });
        }
    }
    };
</script>