<template>
  <div id="form-wrapper">
    <form id="form">
      <div class="flex-wrapper">
        <div>
          <input type="button"
                 @click="putTask"
                 id="submit">
        </div>
        <div style="flex: 6">
          <input type="text"
                 id="title"
                 class="form-control"
                 name="title"
                 v-model="put">
        </div>
      </div>
    </form>
  </div>

</template>

<script>
  import axios from 'axios';

  export default {
    props: ['url'],
    name: 'todo-form',
    data() {
      return {
        put: ''
      };
    },
    methods: {
      putTask() {
        axios
          .post(this.url + 'todo-list/', {title: this.put})
          .then(response => {
            this.$emit('putTask', response.data);
            this.put = '';
          })
          .catch(error => console.log(error));
      }
    }
  };
</script>

<style scoped>
  #form-wrapper {
    position: -webkit-sticky;
    position: sticky;
    top: 0rem;
    padding: 20px;
  }

  #submit {
    margin-top: 20%;
    background-image: url("../assets/put.png");
    width: 25px;
    padding: 0;
    margin-right: 10px;
    border: none;
    font: inherit;
    color: inherit;
    background-color: transparent;
  }

  .flex-wrapper {
    display: flex;
  }

  .flex-wrapper {
    margin: 5px;
    padding: 20px;
    cursor: pointer;
    color: #686868;
  }
</style>
