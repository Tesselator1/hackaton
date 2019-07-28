<template lang="pug">
  #app
    .card(v-for="part in parts")
      .card-header
        button.btn.btn-clear.float-right(@click="deletePart(part)")
        .card-title {{ part.name }}
      .card-body {{ part.params }}
</template>
<script>
import { mapGetters } from 'vuex'
export default {
  name: 'part-list',
  computed: mapGetters(['parts']),
  methods: {
    deletePart (part) {
      this.$store.dispatch('deletePart', part)
    }
  },
  beforeMount () {
    this.$store.dispatch('getParts')
  }
}
</script>
<style>
  header {
    margin-top: 50px;
  }
</style>
