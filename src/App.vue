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

         <v-menu bottom left>
            <template v-slot:activator="{ on, attrs }">
              <v-btn
                light
                icon
                v-bind="attrs"
                v-on="on"
              >
                <v-icon>mdi-account</v-icon>
              </v-btn>
            </template>

            <v-list>
              <v-list-item
                v-for="(item, i) in items"
                :key="i"

                @click="true"
              >
              <a href="/accounts/logout/">
                <v-list-item-title>{{ item.title }}</v-list-item-title>
                <v-icon>{{ item.icon }}</v-icon></a>
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
       items: [
          { title: 'Configuracion', icon: 'mdi-cog-outline' },
          { title: 'Logout', icon: 'mdi-logout-variant' }
        ],
        right: null
    //
  })
};
</script>
