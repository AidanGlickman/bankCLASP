<template>
  <b-container>
    <h1>Students</h1>
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
      <li v-for="student in filteredStudents" v-bind:key="student.email">
        <nuxt-link :to="'/user/' + student.id" v-html="student.name"></nuxt-link>
      </li>
    </ul>
  </b-container>
</template>

<script>
import getData from "../../lib/get-data";
import fuzzy from "fuzzy";
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
    const students = Object.keys(users)
      .map(id => ({ ...users[id], id }))
      .filter(user => user.year)
      .sort((a, b) => {
        if (a.name > b.name) return 1;
        if (a.name < b.name) return -1;
        return 0;
      });
    return {
      students
    };
  },
  computed: {
    filteredStudents() {
      if (!this.filters.name) {
        return this.students;
      }
      var options = {
        pre: "<strong>",
        post: "</strong>",
        extract: function(el) {
          return el.name;
        }
      };
      return fuzzy
        .filter(this.filters.name, this.students, options)
        .map(res => {
          return { ...res.original, name: res.string };
        });
    }
  }
};
</script>