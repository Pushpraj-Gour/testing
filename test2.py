from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

# Define the API router for campaigns
router = APIRouter()

# Create a model to define the structure of the campaign
class Campaign(BaseModel):
    campaign_name: str
    brand_name: str

# In-memory storage for campaigns (for demonstration purposes)
campaigns_db = []

@router.post("/create_campaign")
async def create_campaign(campaign: Campaign):
    # Check if campaign with the same name already exists
    for existing_campaign in campaigns_db:
        if existing_campaign['campaign_name'] == campaign.campaign_name:
            raise HTTPException(status_code=400, detail="Campaign with this name already exists")

    # Add the new campaign to the database (for demo, we are using a list)
    new_campaign = {
        "campaign_name": campaign.campaign_name,
        "brand_name": campaign.brand_name
    }
    campaigns_db.append(new_campaign)

    return {"message": "Campaign created successfully", "campaign": new_campaign}
# adtyhxfghfx