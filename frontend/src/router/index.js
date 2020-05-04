import Vue from "vue";
import Router from "vue-router";
import Home from "@/components/HomepageContent";
import Tool from "@/components/Results";

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
  ],
});
