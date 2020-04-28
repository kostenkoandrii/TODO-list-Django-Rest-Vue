<template>
  <div id="list-wrapper">
    <div v-for="(task, index) in tasks">
      <div class="task-wrapper flex-wrapper">
        <div style="flex: 1">
          <input type="button"
                 id="status_true"
                 @click="updateStatus(task.id, false, index)"
                 v-if="task.completed">
          <input type=button
                 id="status_false"
                 @click="updateStatus(task.id, true, index)" v-else>
        </div>
        <div class="task" style="flex: 6">
                <span class="done_task"
                      v-if="task.completed">{{task.title}}</span>
                <span v-else>{{task.title}}</span>
        </div>
        <div class="button_wrapper"
             style="flex: 1">
          <input class="delete"
                 type="button"
                 v-on:click="deleteTask(task.id, index)">
        </div>
      </div>
    </div>
    <todoForm :url="url" @putTask="pushTask"></todoForm>
  </div>
</template>

<script>
  import todoForm from './todo-form'
  import axios from 'axios'

  export default {
    components: {
      todoForm
    },
    name: 'todo-list',
    data() {
      return {
        tasks: [],
        url: 'http://127.0.0.1:8000/api/'
      };
    },
    created() {
      this.getTasks();
    },
    methods: {
      getTasks() {
        axios
          .get(this.url + 'todo-list/')
          .then(response => {
            this.tasks = response.data;
          })
          .catch(error => console.log(error));
      },

      deleteTask(id, index) {
        axios
          .delete(this.url + 'todo-delete/' + id)
          .then(response => {
            console.log(response.data),
              this.tasks.splice(index, 1);
          })
          .catch(error => console.log(error));
      },

      updateStatus(id, status, index) {
        axios
          .post(this.url + 'todo-completed-update/' + id, {completed: status})
          .then(response => {
            this.tasks[index].completed = response.data.completed;
          })
          .catch(error => console.log(error));
      },

      pushTask(data) {
        if (data.title) {
          this.tasks.unshift(data);
        }
      }
    }
  };
</script>

<style>
  .task-wrapper {
    padding: 2px;
    margin-left: 27px;
    padding-left: 20px;
  }

  #status_true {
    background-image: url("../assets/done_button.png");
    background-size: cover;
    padding: 0;
    margin-top: 7px;
    width: 35px;
    height: 35px;
    margin-right: 5px;
    border: none;
    font: inherit;
    color: inherit;
    background-color: white;
  }

  #status_false {
    background-size: cover;
    padding: 0;
    width: 35px;
    height: 35px;
    margin-right: 5px;
    margin-top: 7px;
    border: 4px solid black;
    border-radius: 20px;
    font: inherit;
    color: inherit;
    background-color: white;
  }

  .task {
    text-align: left;
    color: black;
    margin-top: 12px;
  }

  .done_task {
    font-style: italic;
  }

  .button_wrapper {
    margin-right: 17px;
  }

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
    cursor: pointer;
    color: #686868;
  }

  .delete {
    margin-top: 7px;
    width: 35px;
    height: 35px;
    background-image: url("../assets/delete.png");
    background-size: cover;
    border: none;
    font: inherit;
    color: inherit;
    background-color: transparent;
  }
</style>

