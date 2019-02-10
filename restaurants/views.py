from django.shortcuts import render

def welcome(request):
    return render(request, 'index.html', {'msg':'Hello World!'})

def restaurant_list(request):

    context = {

    	"my_list":[
			{
				
				"restaurant_name":"Alderah",
				"food_type":"Saudi Kabsa"
			},
			{
				
				"restaurant_name":"Italin Hot Hot",
				"food_type":"Spicy Pizza"
			},
			{
				
				"restaurant_name":"Indian Pot",
				"food_type":"Indian Food"
			},
	    ],
    }
    return render(request, 'list.html', context)


def restaurant_detail(request):

    context = {

    		"my_object":
    			{
    				"restaurant_name":"Chipotle",
    				"food_type":"Mexican American Food"
    			}

    }
    return render(request, 'detail.html', context)
