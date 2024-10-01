from fastapi import FastAPI,APIRouter, Depends, HTTPException, Header
from pydantic import BaseModel
from auth_util import bearer_auth  

# Define the API router for campaigns
app = FastAPI
router = APIRouter()

# Create a model to define the structure of the campaign input
class Campaign(BaseModel):
    campaign_name: str
    brand_name: str

campaigns_db = []

@router.post("/create_campaign")
async def create_campaign(campaign: Campaign, user_id: str = Depends(bearer_auth)):

    # Check if a campaign with the same name already exists
    for existing_campaign in campaigns_db:
        if existing_campaign['campaign_name'] == campaign.campaign_name:
            raise HTTPException(status_code=400, detail="Campaign with this name already exists")

    # Add the new campaign to the in-memory database
    new_campaign = {
        "campaign_name": campaign.campaign_name,
        "brand_name": campaign.brand_name,
        "created_by": user_id  # Store the user ID from Bearer auth
    }
    campaigns_db.append(new_campaign)

    return {"message": "Campaign created successfully", "campaign": new_campaign}
