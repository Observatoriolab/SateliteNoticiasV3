<template>
  <v-container>
    <v-row >

      <v-col class="mb-4" cols="4">
        <h1 class="display-2 font-weight-bold mb-3">
          Noticias Trending
        </h1>

        <p class="subheading font-weight-regular">
          For help and collaboration with other Vuetify developers,
          <br />please join our online
          <a href="https://community.vuetifyjs.com" target="_blank"
            >Discord Community</a
          >
        </p>
        <p class="parrafo">Lorem ipsum dolor sit amet consectetur adipisicing elit. Numquam suscipit rerum maxime? Voluptate pariatur debitis voluptatibus, provident quos quidem deserunt. Ipsum officia sint et sapiente fugit inventore labore, incidunt eum?
        Sit incidunt neque, doloremque dolore, nemo veritatis obcaecati facilis distinctio quaerat nostrum dolorum quidem fugiat nihil quasi ullam sed deserunt quisquam nulla numquam. Quis veniam officia optio corporis sequi facilis.
        Repellendus excepturi autem est tempore veritatis tenetur velit at aliquam quisquam dolor. Architecto ipsa animi, nobis voluptatem eius rem error et harum laboriosam eum quam magni fugiat beatae similique totam!
        Repellat, iusto et? Explicabo, consectetur illum? Perferendis fugit eos blanditiis fuga, hic qui veritatis similique at unde accusantium a aut sequi distinctio, dolore eligendi, sed quibusdam id animi expedita necessitatibus!
        Rem sunt provident nulla voluptate illum excepturi in tempora vero cum facilis. Sint est aspernatur atque, iusto libero dolor eos ducimus. Laborum qui tempora modi deleniti quam harum vitae impedit.</p>
        <p class="parrafo">Lorem ipsum dolor sit amet consectetur adipisicing elit. Voluptatibus cumque omnis sunt similique dolorum ipsum ducimus, laboriosam inventore ut amet soluta porro vel eius commodi saepe magnam aliquid maxime tempora.
        Aliquid autem architecto voluptatibus repudiandae? Dolores illum recusandae tempore eaque iure eveniet maxime eum aut unde laboriosam harum quae soluta sint praesentium voluptas, temporibus itaque doloremque quisquam officiis impedit quidem.
        Blanditiis iusto aliquid amet eum culpa, vel repellendus cumque laboriosam minima quibusdam corrupti nemo facilis fugit tempora adipisci tenetur quasi non distinctio hic consequatur itaque commodi, nesciunt voluptatum. Soluta, magni.</p>
        <p class="parrafo">Lorem ipsum dolor sit amet consectetur adipisicing elit. Incidunt qui explicabo in eum eius nam soluta quo, pariatur vitae, similique tenetur sunt commodi corporis ratione, aliquid ducimus ipsam quisquam recusandae.Quasi, architecto repudiandae, ut rerum consequatur voluptas saepe quam dolorem eius repellat voluptatibus. Perspiciatis, ut. Ipsa, recusandae quo. Officiis explicabo amet rerum voluptate quis, animi voluptas illum aspernatur eius tempora.</p>
        <p class="parrafo">Lorem ipsum dolor sit amet consectetur adipisicing elit. Voluptates vero consectetur incidunt aspernatur fugit, mollitia sequi fugiat aliquam esse rem neque excepturi suscipit, ut praesentium aperiam aut officiis a commodi?
        </p>
        <p class="parrafo">Lorem ipsum dolor sit amet consectetur adipisicing elit. Nulla cum aspernatur asperiores ullam laudantium est tempore excepturi eius odio reprehenderit veniam optio sed totam provident, libero obcaecati aliquid distinctio blanditiis.</p>
      </v-col>
      <v-col cols="8" class="text-center mb-4">
        <h1 class="display-2 font-weight-bold mb-7">
          NEWS FEED
        </h1>
        <v-card  class="d-inline-block mx-auto mb-12" raised width="65%" v-for="(item, i) in importantLinks"
                :key="i">
                 <v-container>
              <v-row >
                <v-col cols="4">
                  <v-img
                    height="100%"
                    width="100%"
                    src="https://cdn.vuetifyjs.com/images/cards/store.jpg"
                  ></v-img>
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
                      {{item.text}}
                    </v-col>

                    <v-col class="px-0">
                      <v-row justify="space-around">
                        <font>autor</font>
                        <font>fecha</font>
                          

                      </v-row>
                    </v-col>

                    <v-col class="px-0 mb-0">
                      <p>{{item.href}}</p>
                    </v-col>

                    <v-col class="px-0 mb-0">
                      <v-row justify="space-around">
                       <v-btn icon>
                        <v-icon>mdi-eye</v-icon>
                        300
                      </v-btn>
                      <div class="text-center">
                        <v-rating half-increments hover ripple  v-model="rating"></v-rating>
                      </div>
                      <v-btn icon>
                        <v-icon>mdi-square-edit-outline</v-icon>
                      </v-btn>
                      <v-btn icon>
                        <v-icon>mdi-arrow-expand-all</v-icon>
                      </v-btn>
                          

                      </v-row>
                   
                    </v-col>
                  </v-row>
                </v-col>
              </v-row>
            </v-container>
                
                </v-card>
           <v-card >
           
          </v-card>
          
    </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: "HelloWorld",

  data: () => ({
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
  })
};
</script>
