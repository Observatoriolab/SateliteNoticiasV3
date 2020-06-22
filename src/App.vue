<template>
  <v-app>
     <v-app-bar
      id="home-app-bar"
      app
      color="white"
      elevation="1"
      height="80"
    >
      <v-img
        :src="require('@/assets/logo.svg')"
        class="mr-3 hidden-xs-only"
        contain
        max-width="52"
        width="100%"
      />

      <v-img
        :src="require('@/assets/zero-logo-light.svg')"
        contain
        max-width="128"
        width="100%"
      />

      <v-spacer />

      <div>
        <v-tabs
          class="hidden-sm-and-down"
          optional
        >
          <v-tab
            v-for="(category, i) in categories"
            :key="i"
            :ripple="false"
            active-class="text--primary"
            class="font-weight-bold"
            min-width="96"
            text
          >
            {{ category }}
            
          </v-tab>
        </v-tabs>
      </div>
      <v-spacer />

       <v-menu
          transition="slide-y-transition"
          
          >
            <template v-slot:activator="{ on, attrs }">
              <v-btn
                class="purple"
                color="primary"
                dark
                v-bind="attrs"
                v-on="on"
                
              >
                <v-icon>mdi-account</v-icon>
                {{requestUser}}
              </v-btn>
            </template>
             <v-list >
                  <v-list-item
                    v-for="item in accountItems"
                    :key="item.title"
                  >
                      <v-btn >
                        <a :href="item.ref"><v-icon>  {{ item.icon }}   </v-icon> {{item.title}} </a>
                      </v-btn>
                
                  </v-list-item>
                </v-list>
          </v-menu>
        
    </v-app-bar>

    <v-content>
      <MainPage />
    </v-content>
  </v-app>
</template>

<script>
import MainPage from "./components/MainPage";
import { apiService } from "@/common/api.service.js";
require('@/assets/main.css')

export default {
  name: "App",

  components: {
    MainPage
  },

  data: () => ({
     categories: [
        "Big Data",
        "Pagos Digitales",
        "CBCD",
        "Criptoactivos",
        "Banca abierta",
        "Ciberseguridad",
        "Monitoreo tecnologico",
        "DLT"
      ],
      accountToggle:false,
      accountItems: [
          { title: 'My Account', icon: 'mdi-account',ref:'' },
          { title: 'Log out', icon: 'mdi-logout', ref:'/accounts/logout/' },
      ],
      items: [
        { title: 'Configuracion', icon: 'mdi-cog-outline' },
        { title: 'Logout', icon: 'mdi-logout-variant' }
      ],
      requestUser:null
         
    //
  }),
   methods: {
    //En ves de usar .then, dejarlo asincrono
    async setUserInfo() {
      const data = await apiService("/api/user/");
      const requestUser = data["username"];
      console.log(requestUser)
      //Lo deje en el local storage del browser para ser usado y corroborar que es el usuario
      window.localStorage.setItem("username", requestUser);
      this.requestUser = requestUser
    }
  },
  created() {
    this.setUserInfo();
  }
};
</script>
