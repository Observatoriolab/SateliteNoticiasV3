<template>
  <v-container fluid v-bind:class="{cancelOverflow: edit}">
    <v-row fluid class="mt-3">
        <div   v-show="!drawer && !edition">
            <v-btn  contained
                    fab
                    fixed
                    color="pink"
                    dark
                    large
                    @click.stop="trendingDrawerOpen"
                >
                    <v-icon>mdi-trending-up</v-icon>
            </v-btn>

        </div>
        <v-btn v-show="drawer && !edition"
              contained
              fab
              fixed
              right              
              color="pink"
              dark
              large
              
              @click.stop="trendingDrawerClose"
            >
              <v-icon>mdi-window-minimize</v-icon>
        </v-btn>
         <v-btn v-show="drawer && edition"
              contained
              fab
              fixed
              left              
              color="pink"
              dark
              large
              
              @click.stop="trendingDrawerClose"
            >
              <v-icon>mdi-window-minimize</v-icon>
        </v-btn>
        <v-col v-show="drawer" :cols="newsFeedColumn" class="text-center mb-4">
                  <h1 class="display-2 font-weight-bold mb-7 acolor">
                    TRENDING
                  </h1>
                  
                  <v-card   class="flex-column mx-auto mt-6 mb-6 elevation-12"  width="60%" 
                        v-for="(item,i) in news"
                        :key="i">

                          <v-container :class="{highlight: selected2[i]}">
                              <v-row >
                              
                                <v-col
                                  cols="12"
                                  class="text-center pl-0 px-0 py-0"
                                >
                                  <v-row
                                    class="flex-column ma-0 fill-height text-center"
                                    justify="center"
                                  >
                                    <v-col class="px-0 py-0 text-center" >
                                      <v-card-title style="display:flex; justify-content:center">

                                            {{item.title}}


                                      </v-card-title>


                                    </v-col>

                                    <v-col class="px-0 py-0">
                                      <v-row justify="space-around">
                                        <font class="lighto">autor</font>
                                        <font>fecha</font>
                                          

                                      </v-row>
                                    </v-col>

                                    <v-col class="px-0 py-0 mb-0">

                                          <div class="content" v-html="item.content">
                                          </div>

                                    </v-col>

                                    <v-col class="px-0 py-0">
                                      <v-row justify="space-around" align="center">

                                              <div class="text-center">
                                                <v-rating half-increments hover ripple  dense  v-model="rating"></v-rating>
                                              </div>
                                              <v-btn color="blue" @click="openEdition2(item,i)" :disabled="disabling2[i]">
                                                <v-icon>mdi-square-edit-outline</v-icon>
                                              </v-btn>
                                               <v-btn
                                                      color="darkGray"
                                                      @click="expand(i)"
                                                    >
                                                      <v-icon>{{ show[i] ? 'mdi-chevron-up' : 'mdi-chevron-down' }}</v-icon>
                                              </v-btn>   
                                              
                                                                                            
                                      </v-row>
                                  
                                    </v-col>
                                  
                                      
                                  </v-row>
                                </v-col>
                                 <v-col cols="12" class="py-0">
                                      <v-expand-transition >
                                        <div v-show="show[i]" >
                                            <v-divider></v-divider>
                                            <v-row class="px-4 py-0" justify="center" align="center">
                                                <v-col cols="12" class="py-0">
                                                    <v-row justify="space-between">
                                                        <v-col cols="12">
                                                              <h5>Etiquetas</h5>

                                                        </v-col>
                                                        <v-col cols="6">
                                                              <v-text-field 
                                                                          label="Eje"
                                                                          placeholder="Ej: Pagos digitales"
                                                                          outlined
                                                            ></v-text-field>    
                                                              <v-text-field
                                                                          label="Pais/Region"
                                                                          placeholder="Ej: Rusia"
                                                                          outlined
                                                            ></v-text-field> 
                                                        </v-col>
                                                        <v-col cols="6">
                                                          <v-text-field
                                                                        label="Organismo"
                                                                        placeholder="Ej: FinTech"
                                                                        outlined
                                                          ></v-text-field> 
                                                            <v-text-field
                                                                        label="Fecha"
                                                                        placeholder="Placeholder"
                                                                        outlined
                                                          ></v-text-field>  
                                                        </v-col>

                                                    </v-row>

                                                </v-col>
                                                <v-col  align-self="start" cols="12" class="py-0">
                                                    <v-combobox
                                                          v-model="modelo"
                                                          :filter="filter"
                                                          :hide-no-data="!search"
                                                          :items="comboItems"
                                                          :search-input.sync="search"
                                                          hide-selected
                                                          label="Search for an option"
                                                          multiple
                                                          small-chips
                                                          solo
                                                        >
                                                          <template v-slot:no-data>
                                                            <v-list-item>
                                                              <span class="subheading">Create</span>
                                                              <v-chip
                                                                :color="`${colors[nonce - 1]} lighten-3`"
                                                                label
                                                                small
                                                              >
                                                                {{ search }}
                                                              </v-chip>
                                                            </v-list-item>
                                                          </template>
                                                          <template v-slot:selection="{ attrs, item, parent, selected }">
                                                            <v-chip
                                                              v-if="item === Object(item)"
                                                              v-bind="attrs"
                                                              :color="`${item.color} lighten-3`"
                                                              :input-value="selected"
                                                              label
                                                              small
                                                            >
                                                              <span class="pr-2">
                                                                {{ item.text }}
                                                              </span>
                                                              <v-icon
                                                                small
                                                                @click="parent.selectItem(item)"
                                                              >close</v-icon>
                                                            </v-chip>
                                                          </template>
                                                          <template v-slot:item="{ index, item }">
                                                            <v-text-field
                                                              v-if="editing === item"
                                                              v-model="editing.text"
                                                              autofocus
                                                              flat
                                                              background-color="transparent"
                                                              hide-details
                                                              solo
                                                              @keyup.enter="edit(index, item)"
                                                            ></v-text-field>
                                                            <v-chip
                                                              v-else
                                                              :color="`${item.color} lighten-3`"
                                                              dark
                                                              label
                                                              small
                                                            >
                                                              {{ item.text }}
                                                            </v-chip>
                                                            <v-spacer></v-spacer>
                                                            <v-list-item-action @click.stop>
                                                              <v-btn
                                                                icon
                                                                @click.stop.prevent="edit(index, item)"
                                                              >
                                                                <v-icon>{{ editing !== item ? 'mdi-pencil' : 'mdi-check' }}</v-icon>
                                                              </v-btn>
                                                            </v-list-item-action>
                                                          </template>
                                                  </v-combobox>

                                                </v-col>
                                                <v-col class="text-center py-0" cols="12" >
                                                    <h5>Bibliografia</h5>
                                                </v-col>
                                                <v-col cols="6">

                                                          <v-autocomplete
                                                            v-model="modelo2"
                                                            :items="states"
                                                            :filter="customFilter"
                                                          
                                                            item-text="name"
                                                            label="Nombre"
                                                          ></v-autocomplete>
                                                  
                                                </v-col>
                                                <v-col cols="6">
                                                    <v-text-field
                                                                    label="Link"
                                                                    
                                                      ></v-text-field>          
                                                  

                                                </v-col>


                                            </v-row>
                                        </div>
                                      </v-expand-transition>
                                 </v-col>
                              </v-row>
                          </v-container>
                          
                      </v-card>
                    
        </v-col>

        <v-col v-show="(!drawer && !edition) || (!drawer && edition)" :cols="newsFeedColumn" class="text-center mb-4" >              
                <h1 class="display-2 font-weight-bold mb-7">
                      
                  NEWS FEED
                </h1>              
                <v-card class="flex-column mx-auto mt-6 mb-6 elevation-12" raised width="60%"
                        v-for="(item,i) in news"
                        :key="i">
                    <v-container :class="{highlight: selected[i]}">
                        <v-row >
                          
                          <v-col
                            cols="12"
                            class="text-center pl-0 px-0 py-0"
                          >
                            <v-row
                              class="flex-column ma-0 fill-height text-center"
                              justify="center"
                            >
                              <v-col class="px-0 py-0 text-center">
                                <v-card-title style="display:flex; justify-content:center">

                                    {{item.title}}


                                </v-card-title>


                              </v-col>

                              <v-col class="px-0 py-0">
                                <v-row justify="space-around">
                                  <font class="lighto">autor</font>
                                  <font>fecha</font>
                                    

                                </v-row>
                              </v-col>

                              <v-col class="px-0 py-0 mb-0">

                                    <div  class="content"   
                                          v-html="item.content">
                                    </div>

                              </v-col>

                              <v-col class="px-0 py-1">
                                <v-row justify="space-around" align="center" >

                                         
                                        <div class="text-center">
                                          <v-rating half-increments hover ripple  dense  v-model="rating"></v-rating>
                                        </div>
                                         <v-btn color="blue"  @click="openEdition(item,i)" :disabled="disabling[i]">
                                          <v-icon>mdi-square-edit-outline</v-icon>
                                        </v-btn>
                                          <v-btn 
                                                
                                                color="darkGray"
                                                @click="expand2(i)"
                                                
                                          >
                                            <v-icon>{{ show2[i] ? 'mdi-chevron-up' : 'mdi-chevron-down' }}</v-icon>
                                          </v-btn>
                                       
                                        
                                </v-row>
                              </v-col>
                            </v-row>
                          </v-col>
                          <v-col cols="12" class="py-0">
                              <v-expand-transition >
                                <div v-show="show2[i]" >
                                    <v-divider></v-divider>
                                    <v-row class="px-4 py-0" justify="center" align="center">
                                        <v-col cols="12" class="py-0">
                                            <v-row justify="space-between">
                                                <v-col cols="12">
                                                       <h5>Etiquetas</h5>

                                                </v-col>
                                                <v-col cols="6">
                                                      <v-text-field 
                                                                  label="Eje"
                                                                  placeholder="Ej: Pagos digitales"
                                                                  outlined
                                                    ></v-text-field>    
                                                      <v-text-field
                                                                  label="Pais/Region"
                                                                  placeholder="Ej: Rusia"
                                                                  outlined
                                                    ></v-text-field> 
                                                </v-col>
                                                <v-col cols="6">
                                                  <v-text-field
                                                                label="Organismo"
                                                                placeholder="Ej: FinTech"
                                                                outlined
                                                  ></v-text-field> 
                                                    <v-text-field
                                                                label="Fecha"
                                                                placeholder="Placeholder"
                                                                outlined
                                                  ></v-text-field>  
                                                </v-col>

                                            </v-row>

                                        </v-col>
                                        <v-col  align-self="start" cols="12" class="py-0">
                                            <v-combobox
                                                  v-model="modelo"
                                                  :filter="filter"
                                                  :hide-no-data="!search"
                                                  :items="comboItems"
                                                  :search-input.sync="search"
                                                  hide-selected
                                                  label="Search for an option"
                                                  multiple
                                                  small-chips
                                                  solo
                                                >
                                                  <template v-slot:no-data>
                                                    <v-list-item>
                                                      <span class="subheading">Create</span>
                                                      <v-chip
                                                        :color="`${colors[nonce - 1]} lighten-3`"
                                                        label
                                                        small
                                                      >
                                                        {{ search }}
                                                      </v-chip>
                                                    </v-list-item>
                                                  </template>
                                                  <template v-slot:selection="{ attrs, item, parent, selected }">
                                                    <v-chip
                                                      v-if="item === Object(item)"
                                                      v-bind="attrs"
                                                      :color="`${item.color} lighten-3`"
                                                      :input-value="selected"
                                                      label
                                                      small
                                                    >
                                                      <span class="pr-2">
                                                        {{ item.text }}
                                                      </span>
                                                      <v-icon
                                                        small
                                                        @click="parent.selectItem(item)"
                                                      >close</v-icon>
                                                    </v-chip>
                                                  </template>
                                                  <template v-slot:item="{ index, item }">
                                                    <v-text-field
                                                      v-if="editing === item"
                                                      v-model="editing.text"
                                                      autofocus
                                                      flat
                                                      background-color="transparent"
                                                      hide-details
                                                      solo
                                                      @keyup.enter="edit(index, item)"
                                                    ></v-text-field>
                                                    <v-chip
                                                      v-else
                                                      :color="`${item.color} lighten-3`"
                                                      dark
                                                      label
                                                      small
                                                    >
                                                      {{ item.text }}
                                                    </v-chip>
                                                    <v-spacer></v-spacer>
                                                    <v-list-item-action @click.stop>
                                                      <v-btn
                                                        icon
                                                        @click.stop.prevent="edit(index, item)"
                                                      >
                                                        <v-icon>{{ editing !== item ? 'mdi-pencil' : 'mdi-check' }}</v-icon>
                                                      </v-btn>
                                                    </v-list-item-action>
                                                  </template>
                                          </v-combobox>

                                        </v-col>
                                        <v-col class="text-center py-0" cols="12" >
                                            <h5>Bibliografia</h5>
                                        </v-col>
                                        <v-col cols="6">

                                                  <v-autocomplete
                                                    v-model="modelo2"
                                                    :items="states"
                                                    :filter="customFilter"
                                                  
                                                    item-text="name"
                                                    label="Nombre"
                                                  ></v-autocomplete>
                                          
                                        </v-col>
                                        <v-col cols="6">
                                            <v-text-field
                                                            label="Link"
                                                            
                                              ></v-text-field>          
                                          

                                        </v-col>


                                    </v-row>
                                </div>
                              </v-expand-transition>
                          </v-col>
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
        <v-col v-if="edition" class="text-center" cols="6">
            <div style="display:flex; flex-flow:column; position:fixed;width:auto; height:85vh">
                <h1 class="display-2 font-weight-bold mb-7">
                  EDITION
                    <v-btn icon
                        style="float:right"
                        x-large
                        color="pink"
                        dark
                        

                        @click.stop="closeEdition(false)"
                      >
                        <v-icon>mdi-close-box</v-icon>
                    </v-btn>
                   
                </h1>
                
                <div class="overflowForY" style="overflow-y:auto" color="grey lighten-5" height="100vh" >                      
                       <v-card  class="flex-column mx-auto mt-2 mb-6 elevation-12"  
                          >
                              <v-container>
                                    <v-row >
                                            <v-col
                                              cols="12"
                                              class="text-center pl-0"
                                            >
                                              <v-row
                                                class="flex-column ma-0 "
                                                justify="center"
                                              >
                                                  <v-col class="px-0 text-center" >
                                                    <v-card-title class="">
                                                          {{item.title}}
                                                    </v-card-title>
                                                  </v-col>

                                                  <v-col style="margin:0; padding:0" class="px-0 mb-0 mt-0">
                                                    <v-row class="px-0 mb-0 mt-0" justify="space-around">
                                                      <font>autor</font>
                                                      <font>fecha</font>
                                                    </v-row>
                                                  </v-col>
                                                  <v-col class="px-0 mb-0">
                                                      <div style="float:right">
                                                        <v-btn 
                                                              color="pink"
                                                              dark
                                                              @click="allowEditing = !allowEditing"
                                                            >
                                                            <v-icon>mdi-pencil</v-icon>
                                                        </v-btn>

                                                      </div>
                                                  </v-col>

                                                  <v-col>
                                                          <v-textarea
                                                                outlined
                                                                name="input"
                                                                label="Edicion"
                                                                :disabled="allowEditing"
                                                          ></v-textarea>
                                                  </v-col>

                                                  <v-col class="px-0 mb-0">

                                                        <div  class="content"   
                                                              v-html="item.content">
                                                        </div>

                                                  </v-col>

                                                  <v-col cols="12">
                                                      
                                                        <v-divider></v-divider>
                                                        <v-row class="pa-4" justify="center" align="center">
                                                            <v-col cols="12">
                                                                <v-row justify="space-between">
                                                                    <v-col cols="12">
                                                                          <h6>Primarias</h6>

                                                                    </v-col>
                                                                    <v-col cols="6">
                                                                             <v-autocomplete
                                                                                  v-model="modelo3"
                                                                                  :items="ejes"
                                                                                  :filter="customFilter"
                                                                                
                                                                                  item-text="name"
                                                                                  label="Eje"
                                                                            ></v-autocomplete>
                                                                             <v-autocomplete
                                                                                    v-model="modelo4"
                                                                                    :items="regiones"
                                                                                    :filter="customFilter"
                                                                                  
                                                                                    item-text="name"
                                                                                    label="Pais/Region"
                                                                             ></v-autocomplete>
                                                                    </v-col>
                                                                    <v-col cols="6">
                                                                          <v-autocomplete
                                                                                v-model="modelo5"
                                                                                :items="organismos"
                                                                                :filter="customFilter"
                                                                              
                                                                                item-text="name"
                                                                                label="Organismo"
                                                                      ></v-autocomplete>
                                                                      <v-menu
                                                                          v-model="menu2"
                                                                          :close-on-content-click="false"
                                                                          :nudge-right="40"
                                                                          transition="scale-transition"
                                                                          offset-y
                                                                          min-width="290px"
                                                                        >
                                                                          <template v-slot:activator="{ on, attrs }">
                                                                            <v-text-field
                                                                              v-model="date1"
                                                                              label="Fecha"
                                                                              prepend-icon="event"
                                                                              readonly
                                                                              v-bind="attrs"
                                                                              v-on="on"
                                                                            ></v-text-field>
                                                                          </template>
                                                                          <v-date-picker v-model="date1" @input="menu2 = false"></v-date-picker>
                                                                        </v-menu>

                                                                    </v-col>

                                                                </v-row>

                                                            </v-col>
                                                            <v-col  align-self="start" cols="12">
                                                                <h6>Secundarias</h6>

                                                                <v-combobox
                                                                      v-model="modelo"
                                                                      :filter="filter"
                                                                      :hide-no-data="!search"
                                                                      :items="comboItems"
                                                                      :search-input.sync="search"
                                                                      hide-selected
                                                                      label="Search for an option"
                                                                      multiple
                                                                      small-chips
                                                                      solo
                                                                    >
                                                                      <template v-slot:no-data>
                                                                        <v-list-item>
                                                                          <span class="subheading">Create</span>
                                                                          <v-chip
                                                                            :color="`${colors[nonce - 1]} lighten-3`"
                                                                            label
                                                                            small
                                                                          >
                                                                            {{ search }}
                                                                          </v-chip>
                                                                        </v-list-item>
                                                                      </template>
                                                                      <template v-slot:selection="{ attrs, item, parent, selected }">
                                                                        <v-chip
                                                                          v-if="item === Object(item)"
                                                                          v-bind="attrs"
                                                                          :color="`${item.color} lighten-3`"
                                                                          :input-value="selected"
                                                                          label
                                                                          small
                                                                        >
                                                                          <span class="pr-2">
                                                                            {{ item.text }}
                                                                          </span>
                                                                          <v-icon
                                                                            small
                                                                            @click="parent.selectItem(item)"
                                                                          >close</v-icon>
                                                                        </v-chip>
                                                                      </template>
                                                                      <template v-slot:item="{ index, item }">
                                                                        <v-text-field
                                                                          v-if="editing === item"
                                                                          v-model="editing.text"
                                                                          autofocus
                                                                          flat
                                                                          background-color="transparent"
                                                                          hide-details
                                                                          solo
                                                                          @keyup.enter="edit(index, item)"
                                                                        ></v-text-field>
                                                                        <v-chip
                                                                          v-else
                                                                          :color="`${item.color} lighten-3`"
                                                                          dark
                                                                          label
                                                                          small
                                                                        >
                                                                          {{ item.text }}
                                                                        </v-chip>
                                                                        <v-spacer></v-spacer>
                                                                        <v-list-item-action @click.stop>
                                                                          <v-btn
                                                                            icon
                                                                            @click.stop.prevent="edit(index, item)"
                                                                          >
                                                                            <v-icon>{{ editing !== item ? 'mdi-pencil' : 'mdi-check' }}</v-icon>
                                                                          </v-btn>
                                                                        </v-list-item-action>
                                                                      </template>
                                                              </v-combobox>

                                                            </v-col>
                                                            <v-col class="text-center" cols="12">
                                                                <h5>Bibliografia</h5>
                                                            </v-col>
                                                            <v-col cols="6">

                                                                      <v-autocomplete
                                                                        v-model="modelo2"
                                                                        :items="states"
                                                                        :filter="customFilter"
                                                                      
                                                                        item-text="name"
                                                                        label="Nombre"
                                                                      ></v-autocomplete>
                                                              
                                                            </v-col>
                                                            <v-col cols="6">
                                                                <v-text-field
                                                                                label="Link"
                                                                                
                                                                  ></v-text-field>          
                                                              

                                                            </v-col>
                                                            <v-col cols="12">
                                                              <v-row justify="center">
                                                                          <v-btn large color="primary">Publicar</v-btn>


                                                              </v-row>
                                                                

                                                            </v-col>
                                                        </v-row>
                                                  </v-col>

                                              </v-row>
                                          </v-col>
                                    </v-row> 
                            </v-container>
                        </v-card>
                      

                </div>
                  
            </div>
        </v-col>       
    </v-row>
  </v-container>
</template>

<script>
import { apiService } from "@/common/api.service.js";

export default {
  name: "MainPage",
  watch: {
      search () {
        // Items have already been loaded
        if (this.items.length > 0) return

        // Items have already been requested
        if (this.isLoading) return

        this.isLoading = true

        // Lazily load input items
        fetch('https://api.publicapis.org/entries')
          .then(res => res.json())
          .then(res => {
            const { count, entries } = res
            this.count = count
            this.entries = entries
          })
          .catch(err => {
            console.log(err)
          })
          .finally(() => (this.isLoading = false))
      },
    
      modelo (val, prev) {
        if (val.length === prev.length) return

        this.modelo = val.map(v => {
          if (typeof v === 'string') {
            v = {
              text: v,
              color: this.colors[this.nonce - 1],
            }

            this.comboItems.push(v)

            this.nonce++
          }

          return v
        })
      },
    },

  data: () => ({
    menu2: false,
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
    drawer: false,
    drawer2:false,
    edition:false,
    edit2:false,
    activator: null,
    attach: null,
    colors: ['green', 'purple', 'indigo', 'cyan', 'teal', 'orange'],
    editing: null,
    index: -1,
    item:null,
    item2:null,
    comboItems: [
      { header: 'Select an option or create one' },
      {
        text: 'Foo',
        color: 'blue',
      },
      {
        text: 'Bar',
        color: 'red',
      },
    ],
    nonce: 1,
    menu: false,
    modelo: [
      {
        text: 'Foo',
        color: 'blue',
      },
    ],
    x: 0,
    search: null,
    y: 0,
    allowEditing:true,


    items: [
      { title: 'Home', icon: 'dashboard' },
      { title: 'About', icon: 'question_answer' },
    ],
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
    ],
    hasSaved: false,
    model: null,
    states: [
      { name: 'Florida', abbr: 'FL', id: 1 },
      { name: 'Georgia', abbr: 'GA', id: 2 },
      { name: 'Nebraska', abbr: 'NE', id: 3 },
      { name: 'California', abbr: 'CA', id: 4 },
      { name: 'New York', abbr: 'NY', id: 5 },
    ],
     ejes: [
      { name: 'Big Data', abbr: 'BD', id: 1 },
      { name: 'Pagos Digitales', abbr: 'PD', id: 2 },
      { name: 'CBCD', abbr: 'CBCD', id: 3 },
      { name: 'Criptoactivos', abbr: 'CA', id: 4 },
      { name: 'Banca abierta', abbr: 'OB', id: 5 },
      { name: 'Ciberseguridad', abbr: 'CS', id: 5 },
      { name: 'Monitoreo Tecnologico', abbr: 'MT', id: 5 },
      { name: 'DLT', abbr: 'DLT', id: 5 },

    ],
     regiones: [
      { name: 'Florida', abbr: 'FL', id: 1 },
      { name: 'Georgia', abbr: 'GA', id: 2 },
      { name: 'Nebraska', abbr: 'NE', id: 3 },
      { name: 'California', abbr: 'CA', id: 4 },
      { name: 'New York', abbr: 'NY', id: 5 },
    ],
     organismos: [
      { name: 'Florida', abbr: 'FL', id: 1 },
      { name: 'Georgia', abbr: 'GA', id: 2 },
      { name: 'Nebraska', abbr: 'NE', id: 3 },
      { name: 'California', abbr: 'CA', id: 4 },
      { name: 'New York', abbr: 'NY', id: 5 },
    ],
    modelo2: null,
    modelo3:null,
    modelo4:null,
    modelo5:null,
    date1: new Date().toISOString().substr(0, 10),
    showEdition:false,
    newsFeedColumn:12,
    selected:[],
    disabling:[],
    selected2:[],
    disabling2:[],
    itemIndexPrior:-1,
    itemIndexActual:0,

    itemIndexPrior2:-1,
    itemIndexActual2:0,
    actualIndex: -1,
    trendingScrollingPosition: 0,
    normalFeedScrollingPosition: 0

  }),

  methods:{
    highlighter(index){
      console.log(index)
      if (this.selected[index] == false) {
        this.$set(this.selected,index, true);
        this.$set(this.disabling,index,true)
      }
      console.log(this.itemIndexPrior)
      if(index !== this.itemIndexPrior){

        this.$set(this.selected,this.itemIndexPrior, false);
        this.$set(this.disabling,this.itemIndexPrior, false);
      }
      

      

    },
    highlighter2(index){
      if (this.selected2[index] == false) {
        this.$set(this.selected2,index, true);
        this.$set(this.disabling2,index,true)
      }
      if(index !== this.itemIndexPrior2){

        this.$set(this.selected2,this.itemIndexPrior2, false);
        this.$set(this.disabling2,this.itemIndexPrior2, false);
      }

      
    },
    closeEdition(closingDrawer){
        this.edition = false
        console.log(this.actualIndex)
        this.newsFeedColumn = 12
        
        if(this.drawer || closingDrawer){
          this.$set(this.selected2,this.actualIndex, false);
          this.$set(this.disabling2,this.actualIndex, false);
        }
        else{
          this.$set(this.selected,this.actualIndex, false);
          this.$set(this.disabling,this.actualIndex, false);
        }
    },
    trendingDrawerOpen(){
      this.drawer = true
      if(this.edition){
        this.edition = false
      }
    },
    trendingDrawerClose(){
      this.drawer = false
      this.closeEdition(true)

    },
    openEdition(item,index){
      console.log("abri la edicion")
      
      this.item = item
      this.actualIndex = index
      this.itemIndexPrior = this.itemIndexActual
      this.itemIndexActual = index
      
      this.edition = true
      console.log(index)
      console.log(this.edition)
      this.newsFeedColumn = 6
      this.highlighter(index)
    },
    openEdition2(item,index){
      console.log("abri la edicion")
      this.item = item
      this.actualIndex = index
      this.itemIndexPrior2 = this.itemIndexActual2
      this.itemIndexActual2 = index
      this.edition = true
      console.log(index)
      console.log(this.edition)
      this.newsFeedColumn = 6
      this.highlighter2(index)
    },
    customFilter (item, queryText) {
        const textOne = item.name.toLowerCase()
        const textTwo = item.abbr.toLowerCase()
        const searchText = queryText.toLowerCase()

        return textOne.indexOf(searchText) > -1 ||
          textTwo.indexOf(searchText) > -1
    },
    save () {
      this.hasSaved = true
    },
    edit (index, item) {
        if (!this.editing) {
          this.editing = item
          this.index = index
        } else {
          this.editing = null
          this.index = -1
        }
      },
      filter (item, queryText, itemText) {
        if (item.header) return false

        const hasValue = val => val != null ? val : ''

        const text = hasValue(itemText)
        const query = hasValue(queryText)

        return text.toString()
          .toLowerCase()
          .indexOf(query.toString().toLowerCase()) > -1
      },
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
        for(let i = 0; i < this.news.length; i++) {
            this.selected.push(false);
            this.disabling.push(false)
            this.selected2.push(false);
            this.disabling2.push(false)
        }
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



  }

  
};
</script>
<style >
.content{
   padding:1em;
    font-size:2rem;
    text-align: justify;
    text-justify: inter-cluster;
}
.acolor{
  color:blue;
}

</style>