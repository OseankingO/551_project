# 551_Python Billper

## Introduction

This program is 551 Python class individual project written by _**Xinghan Qin**_.

Billper is a bill manage application which is designed for small and medium size groups in short, medium and long term. 
As tourist industry develops fast and people have higher life quality requirement, bill sharing and management become the daily work during the trip. 
Also, for students and some young people, rent an apartment or a house together means there would be a bill issue, too. 
Hence, the Billper can relief people from dealing with bills during the happy tour or daily life. 

##

## 

## Features

* Create account

* Save money

* Payment

* Reimbursement submission

* Withdraw

* Bill history

* Delete account

##

## Functions

* **Create account**
  
  Users can create a group to manage the bill by choosing number of people and service term.

  * Number of people
  
    * Minimum size 2
    * maximum size 20

  * Service term
  
    * 3 weeks
    
    * 3 months
    
    * 6 months
    
    * 2 years

* **Save money**

  Member can save money into the group account for further payment and reimburse.

  * Saving requirement
  
    Members in the group can submit a save in requirement. 
    The requirement will include who need to save and how much need to save. 
    After everyone involved in the requirement accept, they need to save the required money into the group account. 
    If more than half of payers refuse to save in, the requirement will be cancelled. 
    If at least one but less than half payer refuse to save in, this requirement will be hold and the payers refused have another chance to vote. 
    After the second vote, unless every payer accept, the requirement will be accepted, and it will move to saving part. 
    Otherwise, the requirement will be cancelled.
    
    Saving requirement can be cancelled by the publisher anytime before the requirement being accepted.
    
      * Choose payer (can select individuals or select all)
      
      * Enter the money required from payer
  
  * Saving into account
  
    After requirement being accepted, payer included in requirement need to save the required money into the group account. 
    
    (*further development: 1. if anyone want to cancel the payment during the saving part.* 
    *2. if anyone did not save the money into account after long time*)
    
  * E-receipt will be created and stored in history

* **Payment**

  Member can pay through the app by using group account directly.
  
  (*further development: 1. how to get the limits authority conveniently.* 
  *2. the port to third payment apps or companies*)
  
    * Payment
    
    * E-receipt will be created and stored in history

* **Reimbursement submission**

  Member can submit reimbursement requirement with title, amount of money and receipt. After everyone in group accept the requirement, moneny will be sent back to the publisher's account. If more than half of payers refuse, the requirement will be cancelled. If at least one but less than half payer refuse, this requirement will be hold.
  
  (*further development: 1. better vote rule for at least one but less than half payer refuse situation*)
  
    * Reimbursement requirement
    
      * Title: describe of reimbursement

      * Amount: Money required

      * Picture: receipt photo or copy
    
    * Money send back
    
    * E-receipt will be created and stored in history

* **Withdraw**

  Members can withdraw from group account. 
  The money will be separated equally and send back to all the members' account. 
  Depends on the group type (service term), the group will have different limited withdraw chances. 
  If the group wants extra withdraw chance, it will charge some service fee.
  
    * Withdraw requirement
    
    * Extra withdraw charge (option)
    
    * Pay back
    
    * E-receipt will be created and stored in history
    
* **Bill history**

  Any group member can check and download bill history.
  
  * Check
  
  * Download

* **Delete account**

  Group will be deleted with a all-accepted delete requirement or at expired date. 
  Service will not be available anymore, money in the group account will be automatically send back to members follow the **Withdraw** rule. 
  Bill history will be sent to every member.
  
  * Delete condition
  
    * Delete requirement 

    * Expired date

  * Money send back
  
  * Send Bill history 
  
  * Account delete
  
##

## Design 

##

## Implementations and Methods

* Third payment companies and applications interfaces

    * Save money to group account

    * Payment (need to submit payment requirement to third payment companies and applications and read trade amount.)
    
    * WithDraw from group account

* Service charge

* Money separation 

(*further development*)

##

## Profits and Benefits


* Service fee. When a group is created, depending on the service term, every group member will be charge.

* Extra withdraw fee. Although this charge is mainly used to pay for the trasmit fee to third companies or apps (e.g. bank).

* Advertisement. This app can insert some advertisement.

(*Further development*)

##

## Time Table

(*Further development*)

##

## Author

* Xinghan Qin

##