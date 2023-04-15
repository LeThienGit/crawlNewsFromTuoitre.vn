<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Remote Control</title>

    <!-- Font Awesome -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <!-- CSS -->

    <link rel="stylesheet" href = "style.css">
</head>
<body>
    <input type="checkbox" id="darkmode">
    <div class="mobile">
        <input type="radio" name = "pages" id="page-1">
        <input type="radio" name = "pages" id="page-2">
        <!-- Page 1 -->
        <div class="page_1">
            <!-- Top -->
            <div class="top">
                <i class="fas fa-bars"></i>
                <label for="darkmode" id="darklabel">
                    <i class="fa fa-mood" id="dark-mode" aria-hidden="true"></i>
                </label>
                <i class="fas fa-user"></i>
            </div>

            <!-- Top -->
            <!-- Middle -->
            <div class="middle">
                <div class="hg">
                    <h2>Good Morning <span>:)</span></h2>
                </div>

                <input type="radio" id="info_1"> 
                <input type="radio" id="info_2">
                <input type="radio" id="info_3">

                <!-- Weather infor -->
                <div class="weather-info">
                    <!-- Details -->
                    <div class="details">
                        <div class="w-detail">
                            <i class="fas fa-cloud-sun-rain"></i>
                            <h4>Weather</h4>
                        </div>

                        <div class="w-detail">
                            <h2>21C</h2>
                            <h5>Heat</h5>
                        </div>

                        <div class="w-detail">
                            <h2>83%</h2>
                            <h5>Moisture</h5>
                        </div>
                    </div>
                </div>
                <!-- Weather infor -->

                <!-- cells -->
                <div class="cells">
                    <label for="info_1">
                        <h4>Sat</h4>
                    </label>

                    <label for="info_2">
                        <h4>Sun</h4>
                    </label>

                    <label for="info_3">
                        <h4>Mon</h4>
                    </label>
                </div>
                <!-- / cells -->


                <!-- devices -->
                <div class="devices">
                    <div class="d-master">
                        <h3>4 Devices Connected</h3>
                        <i class="fa fa-info-circle" aria-hidden="true"></i>
                    </div>

                    <!-- device -->
                    <div class="device">
                        <input type="checkbox" id="c1">
                        <label for="c1" id="cc1">
                            <div class="c1">
                                <img src="img/lamp.webp" alt="">
                                <h4>Lamp</h4>
                            </div>
                        </label>

                        <input type="checkbox" id="c2">
                        <label for="c2" id="cc2">
                            <div class="c1">
                                <img src="img/tv.webp" alt="">
                                <h4>TV</h4>
                            </div>
                        </label>
                    </div>
                    <!-- /device -->

                    <!-- device2 -->
                    <div class="device device-2"></div>   
                        <input type="checkbox" id="c3">
                        <label for="c3" id="cc3">
                            <div class="c1">
                                <img src="img/fan.webp" alt="">
                                <h4>A.C</h4>
                                <span class="on"></span>
                                <h6></h6>
                            </div>
                        </label>

                        <input type="checkbox" id="c4">
                        <label for="c4" id="cc4">
                            <div class="c1">
                                <img src="img/fan.webp" alt="">
                                <h4>WiFi</h4>
                                <span class="off"></span>
                                <h6></h6>
                            </div>
                        </label>
                    <!-- /device2 -->            
                </div>
                <!--/ devices -->
            </div>
        </div>
        <!-- Page 1 -->
    </div>
</body>
</html>
