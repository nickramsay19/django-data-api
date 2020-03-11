<template>
  <div id="app">
    <nav-bar/>

    <div class="container">

      <h4>Tabulated data</h4>
      
      <data-table/>
    </div>
  </div>
</template>

<script>
import NavBar from './components/NavBar.vue'
import DataTable from './components/DataTable.vue'

export default {
  name: 'App',
  components: {
    NavBar, 
    DataTable
  }
}
</script>

<style scoped>
  @import "./assets/normalize.css";
  @import "./assets/skeleton.css";

  .container{
    margin-top: 5em;
  }
</style>
