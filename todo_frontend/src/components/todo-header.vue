<template>
  <div class="head">
    <div class="head_info flex-wrapper">
      <div id="head_title"
           style="flex: 8"><span>TODO list</span></div>
      <div id="head_item"
           style="flex: 1">
        <input type="button"
               class="delete">
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    name: 'header-todo'
  };
</script>

<style scoped>
.head_info {
    background-color: lavender;
    border-radius: 6px;
    padding: 0;
    margin: 0;
  }

  .head {
    padding-bottom: 30px;
    padding-top: 30px;
    margin: 0 30px 0 30px;
  }

  #head_title {
    padding: 0;
    margin-top: 10px;
    vertical-align: middle;
    text-align: left;
    margin-left: 15px;
    color: black;
    font-size: 20px;
  }
</style>
