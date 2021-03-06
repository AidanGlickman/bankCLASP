import Vue from "vue";
import Router from "vue-router";
import Home from "@/components/HomepageContent";
import Tool from "@/components/Results";
import Player from "@/components/Player";
import Contact from "@/components/Contact";



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

      path: "/player/:id",
      name: "player",
      component: Player,
    },
    {
      path: "/contact",
      name: "contact",
      component: Contact,
    },
  ],
});
