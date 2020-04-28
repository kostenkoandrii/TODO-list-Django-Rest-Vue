<template>
  <div id="app">
<!--    <router-view/>-->
    <todoWrapper></todoWrapper>
  </div>
</template>

<script>
  import todoWrapper from './components/todo-wrapper';
export default {
  components: {
    todoWrapper
  },
  name: 'App'
}

</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
