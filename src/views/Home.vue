<template>
  <div class="home">
    <MainPage msg="Welcome to Your Vue.js App" />
  </div>
</template>

<script>
require('@/assets/main.css')

// @ is an alias to /src
import MainPage from "@/components/MainPage.vue";

export default {
  name: "Home",
  components: {
    MainPage
  }
};
</script>
