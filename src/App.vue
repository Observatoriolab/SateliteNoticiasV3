<template>
  <v-app>
     <v-app-bar
      id="home-app-bar"
      app
      color="white"
      elevation="1"
      height="80"
    >   
      <v-spacer />

      <div>
        <v-menu bottom :offset-y="true" :close-on-content-click="false">
        <template v-slot:activator="{ on, attrs }">
            <v-btn
              color="primary"
              dark
              v-bind="attrs"
              v-on="on"
            >
              Dropdown
            </v-btn>
          </template>
          <v-tabs vertical>
                  <v-tab>
                    <v-icon left>mdi-account</v-icon>
                    Option 1
                  </v-tab>
                  <v-tab>
                    <v-icon left>mdi-lock</v-icon>
                    Option 2
                  </v-tab>
                  <v-tab>
                    <v-icon left>mdi-access-point</v-icon>
                    Option 3
                  </v-tab>
            
                  <v-tab-item>
                    <v-card flat>
                      <v-card-text>
                        <p>
                                                   Contenido, botones, etc

                        </p>
            
                      </v-card-text>
                    </v-card>
                  </v-tab-item>
                  <v-tab-item>
                    <v-card flat>
                      <v-card-text>
                        <p>
                          Contenido, botones, etc
                        </p>
            
                       
                      </v-card-text>
                    </v-card>
                  </v-tab-item>
                  <v-tab-item>
                    <v-card flat>
                      <v-card-text>
                        <p>
                          Contenido, botones, etc
                        </p>
            
                      </v-card-text>
                    </v-card>
                  </v-tab-item>
                </v-tabs>
        </v-menu>
      </div>
      <v-spacer />

       <v-menu
          transition="slide-y-transition"
          bottom  :offset-y="true"
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
                        <a :href="item.ref"><v-icon>  {{ item.icon }}   </v-icon> {{item.title}} </a>
                
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
