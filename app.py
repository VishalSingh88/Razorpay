from flask import Flask, render_template, request
app = Flask(__name__)
import razorpay

order_id = "nothing"

@app.route("/")
def welcome():
    return "Hello World"

@app.route("/payment", methods=["POST", "GET"])
def pay():
    amount = "50000"
    client = razorpay.Client(auth=("rzp_test_KZwhPzzWj6Rfox","nUlMszQDkMxdNbfWCsIU0sez"))

    order = client.order.create({'amount':int(amount), 'currency':'INR', 'payment_capture':'1'})
    # print(order['id'])
    order_id = order['id']
    print(order_id)
    # return order_id
    return render_template('pay.html', payment=order)

# @app.route("/success", methods=["GET","POST"])
# def success():
#     return "Thanks For Payment."

@app.route('/success', methods=["GET",'POST'])
def payment_success():
    # payment_id = request.form['razorpay_payment_id']
    # razorpay_order_id = order_id
    # signature = request.form['razorpay_signature']

    # Verify payment signature (refer to Razorpay docs)
    # params_dict = {
    #     'razorpay_order_id': razorpay_order_id,
    #     'razorpay_payment_id': payment_id,
    #     'razorpay_signature': signature
    # }

    # print(payment_id," ",razorpay_order_id," ",signature)
    # client = razorpay.Client(auth=("rzp_test_KZwhPzzWj6Rfox","nUlMszQDkMxdNbfWCsIU0sez"))
    # client.utility.verify_payment_signature(params_dict)  

    # print(request.form)
    # If signature verification is successful, process the payment
    # razorpay_payment_id
    # return "Payment successful!"

    print(request)
    postData = request.form
    data = postData.to_dict()
    print(data)
    return data