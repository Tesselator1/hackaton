<template lang="pug">
  #app
    section.container.grid-960
      .columns
        .column.col-2
        .column.col-8.col-md-12
          header.text-center
            h2 Список деталей
          part-list
        .column.col-2
</template>
<div class="row">
  <div class="large-4 columns">
    <form>
      <div class="row collapse">
        <div class="large-9 columns">
          <input type="search" placeholder="search">
        </div>
        <div class="large-3 columns">
          <span class="postfix"><i class="fi-magnifying-glass"></i></span>
        </div>
      </div>
    </form>
  </div>
</div>
<script>
import ListParts from './components/ListParts'
export default {
  name: 'app',
  components: {
    'part-list': ListParts
  }
}
</script>
<style>
  @import url(https://fonts.googleapis.com/css?family=Eczar);
  @import url(https://fonts.googleapis.com/css?family=Work+Sans);
  body {
    font-family: "Work Sans", "Segoe UI", "Helvetica Neue", sans-serif;
  }
  h1, h2, h3, h4, h5, h6 {
    font-family: "Eczar", sans-serif;
  }
</style>
