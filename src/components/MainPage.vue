<template>
  <v-container>
    <v-row >
      <v-col class="mb-4 text-center" cols="4">
            <h1 class="display-2 font-weight-bold mb-3">
              Noticias Trending
            </h1>

            <v-row class="flex-column"  justify="center" > 
              <v-sheet style="overflow:auto"  color="grey lighten-5" height="75vh" >
                     
                        <v-card  class="d-inline-block mx-auto mt-6 mb-6" raised width="75%" 
                          v-for="(item,i) in importantLinks"
                                :key="i">

                                  <v-container>
                                      <v-row >
                                        <v-col cols="4">
                                          <div v-if="true">
                                              <v-img
                                                  height="100%"
                                                  width="100%"
                                                  src="https://cdn.vuetifyjs.com/images/cards/store.jpg"
                                                ></v-img>


                                          </div>
                                          <div v-else> 
                                              <v-img
                                                  height="100%"
                                                  width="100%"
                                                  src="https://cdn.vuetifyjs.com/images/cards/store.jpg"
                                                ></v-img>

                                          </div>
                                        
                                        </v-col>

                                        <v-col
                                          cols="8"
                                          class="text-center pl-0"
                                        >
                                          <v-row
                                            class="flex-column ma-0 fill-height"
                                            justify="center"
                                          >
                                            <v-col class="px-0" >


                                            </v-col>

                                            <v-col class="px-0">
                                              <v-row justify="space-around">
                                                <font>autor</font>
                                                <font>fecha</font>
                                                  

                                              </v-row>
                                            </v-col>

                                            <v-col class="px-0 mb-0">
                                            


                                            </v-col>

                                            <v-col class="p3">
                                              <v-row justify="space-around" align="center">

                                                            <v-btn icon>
                                                        <v-icon>mdi-eye</v-icon>
                                                        300
                                                      </v-btn>
                                                      <div class="text-center">
                                                        <v-rating half-increments hover ripple  dense small v-model="rating"></v-rating>
                                                      </div>
                                                      <v-btn icon>
                                                        <v-icon>mdi-square-edit-outline</v-icon>
                                                      </v-btn>
                                                      <v-btn icon>
                                                        <v-icon>mdi-arrow-expand-all</v-icon>
                                                      </v-btn>
                                                        <v-btn
                                                              icon
                                                              @click="expand(i)"
                                                            >
                                                              <v-icon>{{ show[i] ? 'mdi-chevron-up' : 'mdi-chevron-down' }}</v-icon>
                                                            </v-btn>
                                                          

                                                      
                                                  
                                              </v-row>
                                          
                                            </v-col>
                                          
                                              
                                          </v-row>
                                        </v-col>
                                        <v-expand-transition>
                                                        <div v-show="show[i]">
                                                          <v-divider></v-divider>

                                                          <v-card-text>
                                                            I'm a thig. But, like most politicians, he promised more than he could deliver. You won't have time for sleeping, soldier, not with all the bed making you'll be doing. Then we'll go with that data file! Hey, you add a one and two zeros to that or we walk! You're going to do his laundry? I've got to find a way to escape.
                                                          </v-card-text>
                                                        </div>
                                                      </v-expand-transition>

                                      </v-row>
                                  </v-container>
                        </v-card>
              </v-sheet>
              
            </v-row>
            

      </v-col>
      <v-col cols="8" class="text-center mb-4">
              <h1 class="display-2 font-weight-bold mb-7">
                NEWS FEED
              </h1>
             
              <v-card  class="d-inline-block mx-auto mt-6 mb-6" raised width="75%" 
                v-for="(item,i) in news"
                      :key="i">

                        <v-container>
                            <v-row >
                             
                              <v-col
                                cols="12"
                                class="text-center pl-0"
                              >
                                <v-row
                                  class="flex-column ma-0 fill-height"
                                  justify="center"
                                >
                                  <v-col class="px-0" >
                                    <v-card-title>

                                    {{item.title}}


                                    </v-card-title>


                                  </v-col>

                                  <v-col class="px-0">
                                    <v-row justify="space-around">
                                      <font>autor</font>
                                      <font>fecha</font>
                                        

                                    </v-row>
                                  </v-col>

                                  <v-col class="px-0 mb-0">

                                        <div style="font-size:1.2em;display:flex; flex-flow:column; justify-content:center; align-items:center"  
                                              v-html="item.content">
                                        </div>

                                  </v-col>

                                  <v-col class="p3">
                                    <v-row justify="space-around" align="center">

                                                  <v-btn icon>
                                              <v-icon>mdi-eye</v-icon>
                                              300
                                            </v-btn>
                                            <div class="text-center">
                                              <v-rating half-increments hover ripple  dense  v-model="rating"></v-rating>
                                            </div>
                                            <v-btn icon>
                                              <v-icon>mdi-square-edit-outline</v-icon>
                                            </v-btn>
                                            <v-btn icon>
                                              <v-icon>mdi-arrow-expand-all</v-icon>
                                            </v-btn>
                                              <v-btn
                                                    icon
                                                    @click="expand2(i)"
                                                  >
                                                    <v-icon>{{ show2[i] ? 'mdi-chevron-up' : 'mdi-chevron-down' }}</v-icon>
                                                  </v-btn>
                                                

                                            
                                        
                                    </v-row>
                                
                                  </v-col>
                                
                                    
                                </v-row>
                              </v-col>
                              <v-expand-transition>
                                    <div v-show="show2[i]">
                                      <v-divider></v-divider>
                                      <v-card-text>
                                        I'm a thig. But, like most politicians, he promised more than he could deliver. You won't have time for sleeping, soldier, not with all the bed making you'll be doing. Then we'll go with that data file! Hey, you add a one and two zeros to that or we walk! You're going to do his laundry? I've got to find a way to escape.
                                      </v-card-text>
                                    </div>
                              </v-expand-transition>

                            </v-row>
                        </v-container>
              </v-card>
                <div class="text-center">
                     <v-btn rounded color="primary" dark
                          @click="getnewsLoadMore"
                          :disabled="disableButton"
                        >Cargar mas</v-btn>
                </div>

      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import { apiService } from "@/common/api.service.js";

export default {
  name: "MainPage",

  data: () => ({
    show: [],
    show2: [],
    rating: null,
    endpoint: "/api/news/",
    news: [],
    updateNews: 0,
    updatedNews: [],
    pageNumbers: [],
    next:null,
    content: null,
    contentFlag:false,
    disableButton:false,
    ecosystem: [
      {
        text: "vuetify-loader",
        href: "https://github.com/vuetifyjs/vuetify-loader"
      },
      {
        text: "github",
        href: "https://github.com/vuetifyjs/vuetify"
      },
      {
        text: "awesome-vuetify",
        href: "https://github.com/vuetifyjs/awesome-vuetify"
      }
    ],
    importantLinks: [
      {
        text: "Documentation",
        href: "https://vuetifyjs.com"
      },
      {
        text: "Chat",
        href: "https://community.vuetifyjs.com"
      },
      {
        text: "Made with Vuetify",
        href: "https://madewithvuejs.com/vuetify"
      },
      {
        text: "Twitter",
        href: "https://twitter.com/vuetifyjs"
      },
      {
        text: "Articles",
        href: "https://medium.com/vuetify"
      }
    ],
    whatsNext: [
      {
        text: "Explore components",
        href: "https://vuetifyjs.com/components/api-explorer"
      },
      {
        text: "Select a layout",
        href: "https://vuetifyjs.com/layout/pre-defined"
      },
      {
        text: "Frequently Asked Questions",
        href: "https://vuetifyjs.com/getting-started/frequently-asked-questions"
      }
    ]
  }),
  methods:{
    expand(i){
      console.log("I was clicked")
      console.log(this.show[i])
      this.$set(this.show,i,!(this.show[i]))
    },
     expand2(i){
      console.log("I was clicked")
      console.log(this.show2[i])
      this.$set(this.show2,i,!(this.show2[i]))
    },
     async delayedNews(item) {
      await apiService(item).then(data => {    
          this.updatedNews.push(...data.results);
      });
    },
    disableLoad(){

    },
    actualContent(contentWithImage){
        console.log(contentWithImage)
        let actualContent = contentWithImage.match(/<img src=".*">/)
        let final = contentWithImage.replace(actualContent,"")
        this.content = final
    },
    async getnews() {
      for (const [idx, url] of this.pageNumbers.entries()) {
        console.log(idx)
        await this.delayedNews(url);
      }
      for (var i = 0; i < this.updatedNews.length; i++) {
        this.$set(this.news, i, this.updatedNews[i]);
      }
      this.updatedNews.splice(0);
      console.log(this.news)
      this.updateNews += 1;
    },
    getLastDigit(pageString) {
      let regex = /=+\d*/.exec(pageString);
      var nuevo = /\d+$/.exec(regex[0]);
      return parseInt(nuevo[0]) - 1;
    },
    async getnewsLoadMore() {
      this.disableButton = true
      if (this.next) {
        this.endpoint = this.next;
      }
      await apiService(this.endpoint).then(data => {
        this.news.push(...data.results);
        if (data.next) {
          this.next = data.next;
          this.pageNumbers.push(
            "/api/news/?page=" + this.getLastDigit(this.next)
          );
          this.disableButton = false
        }
        else if (data.count<=4){
            this.pageNumbers.push(
            "/api/news/?page=1"
          );
        }
         else {
          this.next = null;
        }
     
      });
    },

  },
  created(){
      this.getnewsLoadMore();
    document.title = "Satelite de Noticias";
    console.log("asdasdadsadsdasads")


  }

  
};
</script>
