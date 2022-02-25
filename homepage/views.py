from django.shortcuts import redirect, render

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        curruser = request.user
        return render(request,'landing/homepage.html',{'curr_user' : curruser})
    else:
        return redirect('authentication:signin')

def camera(request):
    if request.user.is_authenticated:
        curruser = request.user

        context = {
            'cameraclick' : 1 ,
            'FoodCheck' : 1 ,
            'userid' : curruser.id,
            'result_img1' : 'TEST/IMAGE/PATH'
        }
        
        return render(request,'camera.html', context)
    
    else:

        return redirect('authentication:signin')