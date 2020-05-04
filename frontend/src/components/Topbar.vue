<template>
  <div class="topnav">
    <div class="row padding black">
      <router-link to="/" class="active">BANKclasp</router-link>
      <a href="#about">About</a>
      <router-link to="/tool">Tool</router-link>
      <a href="#CONTACT US">Contact Us</a>
    </div>
  </div>
</template>

<script>
export default {
  name: "Topbar",
};
</script>

<style lang="css" scoped>
* {
  box-sizing: border-box;
}

body {
  margin: 0;
  font-family: "Courier New", Courier, monospace;
}

.topnav {
  overflow: hidden;
  background-color: #e9e9e9;
}

.topnav a {
  float: left;
  display: block;
  color: black;
  text-align: center;
  padding: 14px 16px;
  text-decoration: none;
  font-family: "Courier New", Courier, monospace;
}

.topnav a:hover {
  background-color: #ddd;
  color: black;
}

.topnav a.active {
  background-color: #75f3c2;
  color: white;
}

.topnav .search-container {
  float: right;
}

.topnav input[type="text"] {
  padding: 6px;
  margin-top: 8px;
  font-size: 17px;
  border: none;
}

.topnav .search-container button {
  float: right;
  padding: 6px;
  margin-top: 8px;
  margin-right: 16px;
  background: #ddd;
  font-size: 17px;
  border: none;
  cursor: pointer;
}

.topnav .search-container button:hover {
  background: #ccc;
}

@media screen and (max-width: 600px) {
  .topnav .search-container {
    float: none;
  }

  .topnav a,
  .topnav input[type="text"],
  .topnav .search-container button {
    float: none;
    display: block;
    text-align: left;
    width: 100%;
    margin: 0;
    padding: 14px;
  }

  .topnav input[type="text"] {
    border: 1px solid #ccc;
  }
}
</style>
