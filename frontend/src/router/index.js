import Vue from "vue";
import Router from "vue-router";
import Home from "@/components/HomepageContent";
import Tool from "@/components/Results";
<<<<<<< HEAD
import Player from "@/components/Player";
=======
import Contact from "@/components/Contact"
>>>>>>> d52083207487390d9f0b95ac69f67862e73559f8

Vue.use(Router);

export default new Router({
  mode: "history",
  routes: [
    {
      path: "/",
      name: "home",
      component: Home,
    },
    {
      path: "/tool",
      name: "tool",
      component: Tool,
    },
    {
<<<<<<< HEAD
      path: "/player/:id",
      name: "player",
      component: Player,
    },
=======
      path: "/contact",
      name: "contact",
      component: Contact,
    }
>>>>>>> d52083207487390d9f0b95ac69f67862e73559f8
  ],
});
