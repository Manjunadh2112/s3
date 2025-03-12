import streamlit as st
import boto3
import json
import os

# AWS S3 details
BUCKET_NAME = "stepfunctionsmessages"  # Replace with your bucket name
FILE_NAME = "301_arn_aws_states_eu-west-1_518923560508_execution_WakeupFarms_StepFunctions_v11_auto-retry_1b67cd00-acc8-4809-ad75-de0ec48c3c33.json"

# Initialize S3 client
s3 = boto3.client("s3")

# Streamlit UI
st.title("Download JSON File from AWS S3")

if st.button("Download JSON File"):
    try:
        # Download the file
        with open(FILE_NAME, "wb") as f:
            s3.download_fileobj(BUCKET_NAME, FILE_NAME, f)

        # Read and display JSON
        with open(FILE_NAME, "r") as f:
            json_data = json.load(f)
            st.json(json_data)  # Display JSON in Streamlit
        
        # Provide download link
        with open(FILE_NAME, "rb") as f:
            st.download_button(
                label="Download JSON File",
                data=f,
                file_name=FILE_NAME,
                mime="application/json"
            )
        
        # Clean up local file
        os.remove(FILE_NAME)

    except Exception as e:
        st.error(f"Error downloading file: {e}")
