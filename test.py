from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

# Define the API router for campaigns
router = APIRouter()

# Create a model to define the structure of the campaign input
class Campaign(BaseModel):
    campaign_name: str
    brand_name: str

# In-memory storage for campaigns (for demonstration purposes)
campaigns_db = []

@router.post("/create_campaign")
async def create_campaign(campaign: Campaign):
    """
    POST API that creates a new campaign.
    Accepts campaign_name (input) and brand_name (dropdown selection) in a single request.
    """
    # Check if a campaign with the same name already exists
    for existing_campaign in campaigns_db:
        if existing_campaign['campaign_name'] == campaign.campaign_name:
            raise HTTPException(status_code=400, detail="Campaign with this name already exists")

    # Add the new campaign to the in-memory database
    new_campaign = {
        "campaign_name": campaign.campaign_name,
        "brand_name": campaign.brand_name
    }
    campaigns_db.append(new_campaign)

    return {"message": "Campaign created successfully", "campaign": new_campaign}
