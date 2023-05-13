
from Lib import Database
from Lib import History
from flask import Blueprint, request
from flask_cors import CORS, cross_origin
from .SaveBusiness import save_business
from .DeleteBusiness import delete_business
from .GetBusiness import get_business
from .GetBusinessHumans import get_BusinessHumans
from .GetHumans import get_Humans
from .SaveBusinessHuman import save_BusinessHuman
from .DeleteBusinessHuman import Delete_BusinessHuman
from .GetRoles import get_roles

blueprint = Blueprint('Business', __name__)

@blueprint.route("/Business/SaveBusiness", methods=['GET'])
@cross_origin()
def SaveBusiness():
    business_data = request.args.to_dict()

    # Extract the BusinessId and BusinessName from the business_data
    BusinessId = business_data.get('BusinessId', None)
    BusinessName = business_data.get('BusinessName', None)

    # Call the save_business function from SaveBusiness.py with the extracted data
    result = save_business(BusinessId, BusinessName)
    History.SaveHistory(business_data,"Business", "BusinessId", result["BusinessId"])

    return result
    
    

@blueprint.route("/Business/DeleteBusiness", methods=['GET'])
@cross_origin()
def DeleteBusiness():
    # Get the business data from the request
    business_data = request.args.to_dict()

    # Get the business ID from the request
    BusinessId = business_data.get('BusinessId')
    # Call the delete_business function from DeleteBusiness.py
    result = delete_business(BusinessId)
    History.SaveHistory(business_data,"Business", "BusinessId",BusinessId)
    return result

@blueprint.route("/Business/GetBusiness", methods=['GET'])
@cross_origin()
def GetBusiness():
    # Get the business data from the request
    business_data = request.args.to_dict()

    # Get the business ID from the request
    BusinessId = business_data.get('BusinessId')
    # Call the get_business function from GetBusiness.py
    result = get_business(BusinessId)
    return result

@blueprint.route("/Business/GetBusinessHumans", methods=['GET'])
@cross_origin()
def GetBusinessHumans():
    # Get the business data from the request
    business_data = request.args.to_dict()

    # Get the business ID from the request
    BusinessId = business_data.get('BusinessId')
    # Call the get_business function from GetBusiness.py
    result = get_BusinessHumans(BusinessId)
    return result

@blueprint.route("/Business/GetHumans", methods=['GET'])
@cross_origin()
def GetHumans():
    # Get the business data from the request
    business_data = request.args.to_dict()

    # Call the get_business function from GetBusiness.py
    result = get_Humans()
    return result

@blueprint.route("/Business/SaveBusinessHuman", methods=['GET'])
@cross_origin()
def SaveBusinessHuman():
    business_data = request.args.to_dict()

    # Extract the BusinessId and BusinessName from the business_data
    BusinessId = business_data.get('BusinessId', None)
    HumanId = business_data.get('HumanId', None)
    RoleId = business_data.get('RoleId', None)

    # Call the save_business function from SaveBusiness.py with the extracted data
    result = save_BusinessHuman(BusinessId, HumanId, RoleId)
    History.SaveHistory(business_data,"BusinessHumans", "BusinessId:HumanId:RoleId", BusinessId+":"+HumanId+":"+RoleId)

    return result

@blueprint.route("/Business/DeleteBusinessHuman", methods=['GET'])
@cross_origin()
def DeleteBusinessHuman():
    # Get the business data from the request
    business_data = request.args.to_dict()

    # Get the business ID from the request
    BusinessId = business_data.get('BusinessId')
    HumanId = business_data.get('HumanId')
    # Call the delete_business function from DeleteBusiness.py
    result = Delete_BusinessHuman(BusinessId,HumanId)
    History.SaveHistory(business_data,"BusinessHumans", "BusinessId:HumanId",BusinessId+":"+HumanId)
    return result

@blueprint.route("/Business/GetRoles", methods=['GET'])
@cross_origin()
def GetRoles():
    # Get the business data from the request
    business_data = request.args.to_dict()

    # Call the get_business function from GetBusiness.py
    result = get_roles()
    return result
@blueprint.route("/Business/LastModified", methods=['GET'])
@cross_origin()
def LastModified():
    # Get the business data from the request
    business_data = request.args.to_dict()

    # Get the business ID from the request
    result = History.LastModified("Business", "BusinessId", business_data.get('BusinessId'))
    return result