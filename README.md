# CIDM-6325-Final-Project
Andrew Bonds CIDM 6325 Final Project Repository

| Feature| Description |
| ----------- | ----------- |
| Authentication | The Django Authentication feature will allow users to create secure passwords allowing them to login |
| SEO Otimization | This is a unique quality of Django that will give Mowers an advantage over rivals. The SEO feature will help by submitting Mowers to a search engine so that it shows up in the top results. |
| High Security | The high security feature of Django ensures that all of our customer data will be secure giving both the customers as well as the company a peace of mind |
| Scalability | As Mowers continues to grow the scalabilty feature will allow for the application to be scaled accordingly in instance of rapid development so users are not inconvinienced|
| Speed/App Performance | Because it provides quick development from concepte to completion rapid updates to any issues that the users might find |
| Intuitive UX | Allows for users to navigate through the Mowers App seamlessly and conviniently |

| Feature | Description of Feature |
| ----------- | ----------- |
| Authentication | Django has authentication automatically built into the framework. This will allow users to securely sign in with a strong password and a Multi Factor Authentication method such as the users cell phone or email for added security ('django.contrib.auth') |
| SEO Optimization | The SEO system that Django uses is one of the most beneficial aspects of using Django. With this, users will be able to find Mowers when searching for relevant searchers (class MyMetadata(seo.Metadata):title       = seo.Tag(head=True, max_length=68) description = seo.MetaTag(max_length=155) keywords    = seo.KeywordTag() heading     = seo.Tag(name="h1") |
| Authentication URL's | Allows for users to login,logout, and manage password urlpatterns += [ path('accounts/', include('django.contrib.auth.urls')),]| 
| Security | To enable extra secuirty for your app you can add the following code <input type="hidden" name="csrfmiddlewaretoken" value="0QRWHnYVg776y2l66mcvZqp8alrv4lb8S8lZ4ZJUWGZFA5VHrVfL2mpH29YZ39PW" /> |
| Intuitive UX | Description of Feature |

| Domain Name | The Domain that will be used for Mowers|
| ----------- | ----------- |
| Mowers Domain Name | http://dingdongmowers.com/ |

| Deployment Method | It is planned to deploy mowers with Heroku |
| ----------- | ----------- |
| Planning on usering Heroku for Mowers | Deploying With Heroku allows for the focus to be solely on making mowers great and not having to worry about the server or networking side of the application. With Heroku the server and networking side is built in |
