# Before

```html
<div id="forgotpassword" class="modal forgotpassword" role="dialog">
                    <div class="modal-dialog ModalDialog">
                      <div class="modal-content ModalContent">
                        <div class="modal-header ModalHeader">
                            <h4 class="ModalHeading">Forgot Password</h4>
                            <button type="button" class="close" data-dismiss="modal">&times;</button>
                        </div>
                        <div class="otpSection">
                          <form class="formcover text-center" autocomplete="off">
                            <h6 class="RgNUmber">Enter Registered Mobile Number </h6>
                            <div class="form-group">
                              <input type="text" name="forgotOtp" id="forgotOtp" class="form-control input-lg enterOtp" placeholder="Enter OTP" 
                              autocomplete="off"/>
                            </div>
                            <div class="form-group text-center">
                              <a name="button" class="btn btn-primary btn-lg btnsubmit">Submit</a>
                            </div>
                          </form>
                        </div>
                        </div>
                    </div>
                  </div>
```

# After

```html
<div className={ "modal " + classes.forgotpassword} id="forgotpassword" role="dialog">
    <div className={ "modal-dialog " + classes.ModalDialog}>
        <div className={ "modal-content " + classes.ModalContent}>
            <div className={ "modal-header " + classes.ModalHeader}>
                <h4 className={classes.ModalHeading}>Forgot Password</h4>
                <button className={ "close"} data-dismiss="modal" type="button">�</button>
            </div>

            <div className={classes.otpSection}>
                <form autocomplete="off" className={classes.formcover + "text-center"}>
                    <h6 className={classes.RgNUmber}>Enter Registered Mobile Number </h6>
                    <div className={ "form-group"}>
                        <input autocomplete="off" className={ "form-control input-lg " + classes.enterOtp} id="forgotOtp" name="forgotOtp" placeholder="Enter OTP" type="text" />
                    </div>
                    <div className={ "form-group text-center"}>
                        <a className={ "btn btn-primary btn-lg " + classes.btnsubmit} name="button">Submit</a>
                    </div>
                </form>
            </div>
        </div>
    </div>
</div>
```