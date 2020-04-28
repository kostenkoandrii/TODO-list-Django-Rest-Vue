<template>
  <div>
    <div class="container">
      <div id="task-container">
        <todoHeader></todoHeader>
        <todoList></todoList>
      </div>
    </div>
  </div>
</template>

<script>

  import todoHeader from './todo-header'
  import todoList from './todo-list';

  export default {
    name: 'todo-wrapper',
    components: {
      todoList, todoHeader
  },
  };
</script>

<style>
  #task-container {
    max-width: 600px;
    margin: 0 auto;
    box-shadow: 0 14px 28px rgba(0, 0, 0, 0.25), 0 10px 10px rgba(0, 0, 0, 0.22);
    background-color: #fff;
    margin-top: 100px;
    margin-bottom: 100px;
    justify-content: space-around;
    align-items: flex-start;
  }
</style>
