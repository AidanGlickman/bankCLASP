<template>
    <div class="HomepageContent">
        <!-- Header with image -->
        <header>
        <!-- Put an image or something here-->
        </header>

        <!-- About Container -->
        <div class="container" id="about">
            <div class="content" style="max-width:700px">
                <h5 class="center padding-64"><span class="tag wide">ABOUT BANKCLASP</span></h5>
                <p>We are a team of highschool students who are working on this project for a capstone class.</p>
                <p>This tool is designed to analyze college football players and give the five NFL players who they have the most similar prospects to. This will allow for the making of informed trade and contract decisions for members of the industry.</p>
                <div class="panel leftbar light-grey">
                    <p>Team members: Brandon Schein, Aidan Glickman, Anthony Alban, Nate Jeffries, Kris Pursianen</p>
                </div>
            </div>
        </div>

        <!-- TOOL container -->
        <div class="container" id="TOOL">
            <div class="content" style="max-width:700px">

                <h5 class="center padding-48"><span class="tag wide">PLAYER LOOKUP HERE</span></h5>

                <div class="searchbar">
                    <input type="text" placeholder="Search..">
                </div>


            </div>
        </div>

        <!-- Contact/Area Container -->
        <div class="container" id="CONTACT US" style="padding-bottom:32px;">
            <div class="content" style="max-width:700px">
                <h5 class="center padding-48"><span class="tag wide">CONTACT US</span></h5>
                <p>Email us at help@bankclasp.com</p>
                <p> or </p>
                <p>Leave us an issue at https://github.com/natjef/bankCLASP</p>
            </div>
        </div>

        <footer><i>Beta Version 0.2</i></footer>
    </div>
</template>

<script>
    export default {
        name: 'HomepageContent'
    }
</script>

<style lang="css" scoped>
</style>