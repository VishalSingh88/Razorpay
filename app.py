from flask import Flask, render_template, request
app = Flask(__name__)
import razorpay

order_id = "nothing"

client = razorpay.Client(auth=("rzp_test_Bs0a1arJo0LHkL","DVurd2KmJ4gGgBk6xAeCOiMI"))

@app.route("/")
def welcome():
    return "Hello World"

@app.route("/payment", methods=["GET"])
def pay():
    amount = "50000"
    

    order = client.order.create({'amount':int(amount), 'currency':'INR', 'payment_capture':'1'})
    print(order)
    print(order['id'])
    order_id = order['id']
    print(order_id)
    # return order_id
    return render_template('pay.html', payment=order)

# @app.route("/success", methods=["GET","POST"])
# def success():
#     return "Thanks For Payment."

@app.route('/success', methods=['POST'])
def payment_success():
    paymentId = request.form['razorpay_payment_id']
    razorpayOrderId = request.form['razorpay_order_id']
    signature = request.form['razorpay_signature']
    # razorpayOrderId = razorpayOrderId[:-1] + "r"

    # Verify payment signature (refer to Razorpay docs)
    paramsDict = {
        'razorpay_order_id': razorpayOrderId,
        'razorpay_payment_id': paymentId,
        'razorpay_signature': signature
    }

    # return paramsDict

    try:
        verify = client.utility.verify_payment_signature(paramsDict)
        # Payment successful, process the order here
        # print("Payment Successful")
        # print(verify)
        return "payment successful"
        # if verify:
         
        #     return "payment successful"
        # elif verify == "Razorpay Signature Verification Failed":
        #     return "payment failed"
        
    except Exception as e:
        # Payment verification failed
        # print("Payment Verification Failed")
        print(e)
        return "failed"


if __name__ == '__main__':
    app.run(debug=True)