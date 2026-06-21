import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA



df = pd.read_csv("data/data.csv")

#for col in df.columns:
    #print(col)
    
# --------------------------------- Data Set Exploration --------------------------------------
#print(df.head())

#print(df.tail())

#print(df.info())
#print(df.shape)
df.describe()


#print(df.columns)

#print(df.dtypes)

#print(df.isnull().sum())
#print(df.isna().sum())


#print(df.duplicated().sum())

#print(df.nunique())


#- ------------------------------------------------------------------------------------------------

# For important categorical columns:

#print(df["Gender"].value_counts())

#print(df["Marital Status"].value_counts())

#print(df["Education Level"].value_counts())

#print(df["Geographic Information"].value_counts())

#print(df["Occupation"].value_counts())

#print(df["Preferred Communication Channel"].value_counts())



# Data Exploration Part Completed

# ------------------------------------Now Data Cleaning-----------------------------------------------

#print(df.isnull().sum())

#print("Duplicate Rerodes:- ",df.duplicated().sum())

df.drop_duplicates(inplace=True)

# Remove Extra Spaces

for col in df.select_dtypes(include="string"):
    df[col] = df[col].str.strip()

# Standarised Column names

df.columns= df.columns.str.strip().str.replace(" ","_")


# Fill missing numerical values with Mean

df["Age"]= df["Age"].fillna(df["Age"].mean())
df["Income_Level"]=df["Income_Level"].fillna(df["Income_Level"].mean())
df["Coverage_Amount"]=df["Coverage_Amount"].fillna(df["Coverage_Amount"].mean())
df["Premium_Amount"]=df["Premium_Amount"].fillna(df["Premium_Amount"].mean())

# Fill missing categorical values with Mode

df["Gender"]=df["Gender"].fillna(df["Gender"].mode()[0])
df["Marital_Status"] = df["Marital_Status"].fillna(df["Marital_Status"].mode()[0])
df["Interactions_with_Customer_Service"]=df["Interactions_with_Customer_Service"].fillna(df["Interactions_with_Customer_Service"].mode()[0])
df["Insurance_Products_Owned"]=df["Insurance_Products_Owned"].fillna(df["Insurance_Products_Owned"].mode()[0])
df["Policy_Type"]=df["Policy_Type"].fillna(df["Policy_Type"].mode()[0])
df["Customer_Preferences"]=df["Customer_Preferences"].fillna(df["Customer_Preferences"].mode()[0])
df["Preferred_Communication_Channel"]=df["Preferred_Communication_Channel"].fillna(df["Preferred_Communication_Channel"].mode()[0])
df["Preferred_Contact_Time"]=df["Preferred_Contact_Time"].fillna(df["Preferred_Contact_Time"].mode()[0])
df["Preferred_Language"]=df["Preferred_Language"].fillna(df["Preferred_Language"].mode()[0])

# ------------------DROP COLUMN THAT CANNOT BE FILLED--------------------------------------

df.dropna(subset=["Customer_ID"],inplace=True)


# ===========================
# Data Visualization
# ===========================


# Histogram - Age Distribution

plt.figure(figsize=(8,4))
plt.hist(df["Age"],bins=20,edgecolor="black")
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.savefig("images/age_distribution.png")
#plt.show()

# Histomgram - Premium Amount

plt.figure(figsize=(8,4))
plt.hist(df["Premium_Amount"],bins=20, edgecolor="black")
plt.title("Premium Amount")
plt.xlabel("Premium Amount")
plt.ylabel("Frequency")
plt.savefig("images/premium_amount.png")
#plt.show()

# Bar Chart - Gender Distribution

gender = df["Gender"].value_counts()

plt.figure(figsize=(8,4))
gender.plot(kind="bar", color="skyblue")
plt.title("Gender Distribution")
plt.xlabel("Gender")
plt.ylabel("Count")
plt.savefig("images/gender_distribution.png")
#plt.show()

# Bar Chart - Education Level

education= df["Education_Level"].value_counts()

plt.figure(figsize=(8,5))

education.plot(kind="bar",color="red")
plt.title("Education Level")
plt.xlabel("Education Level")
plt.ylabel("Count")
plt.savefig("images/education_level.png")
#plt.show()

# Pie Chart - Interactions with Customer Service

Interactions_with_Customer_Service=df["Interactions_with_Customer_Service"].value_counts()

Interactions_with_Customer_Service.plot(kind="pie",figsize=(8,5), autopct="%1.1f%%")
plt.title("Interactions")
plt.ylabel("")
plt.savefig("images/Interactions_with_Customer_Servic.png")
#plt.show()

# -- Bar Chart - Occupation 

occupation = df["Occupation"].value_counts()

plt.figure(figsize=(10,5))
occupation.plot(kind="bar")

plt.title("Occupation Distribution")
plt.xlabel("Occupation")
plt.ylabel("Count")

plt.xticks(rotation=90)
plt.savefig("images/occupation_distribution.png")
#plt.show()

#------Policy Type Pie Chart

policy = df["Policy_Type"].value_counts()

plt.figure(figsize=(7,7))
policy.plot(kind="pie", autopct="%1.1f%%")

plt.title("Policy Type Distribution")
plt.ylabel("")

plt.savefig("images/policy_type.png")
#plt.show()

premium = df.groupby(["Gender", "Policy_Type"])["Premium_Amount"].mean().unstack()

premium.plot(kind="bar", figsize=(8,5))

plt.title("Average Premium by Gender and Policy Type")
plt.xlabel("Gender")
plt.ylabel("Average Premium")
#plt.show()

premium = df.groupby("Age")["Premium_Amount"].mean()

plt.figure(figsize=(10,5))
premium.plot(kind="line",marker="o")

plt.title("Average Premium by Age")
plt.xlabel("Age")
plt.ylabel("Average Premium")

plt.savefig("images/premium_by_age.png")
#plt.show()


# ======================================== Encoding the Categorical Column=================================================

le = LabelEncoder()


categorical_columns = df.select_dtypes(include=["object", "string"]).columns

# Don't encode Customer_ID because it's just an identifier
#categorical_columns = categorical_columns.drop("Customer_ID")

for col in categorical_columns:
    df[col] = le.fit_transform(df[col].astype(str))

#print(df.head())

scaler = StandardScaler()

scaled_data  = scaler.fit_transform(df)

#print(scaled_data[:5])

# ======================What is the Elbow Method?=============================================

#The Elbow Method runs K-Means multiple times.

#n_clusters=i → Current value of K.

#random_state=42 → Gives reproducible results.

#n_init=10 → Runs K-Means 10 times with different initial centroids and keeps the best result. This usually gives more stable clusters.


#WCSS = Within Cluster Sum of Squares

#It measures how compact the clusters are.

wcss=[]

for i in range(1,11):
    kmeans=KMeans(
        n_clusters = i,
        random_state = 42,
        n_init=10
    )
    kmeans.fit(scaled_data)

    wcss.append(kmeans.inertia_)

#=================================== Graph ============================

plt.figure(figsize=(8,5))

plt.plot(range(1,11),wcss, marker="o")
plt.title("Elbow method")
plt.xlabel("Number of Clusters (K)")
plt.ylabel("WCSS")
plt.grid(True)
plt.savefig("images/elbow_method.png")

#plt.show()



kmeans = KMeans(
    n_clusters=4,
    random_state=42,
    n_init=10
)

clusters = kmeans.fit_predict(scaled_data)

df["Clusters"] = clusters

# print(df.head())

# =====================================Next Step: Analyze the Clusters ====================================================



print(df["Clusters"].value_counts())

clustered_summary = df.groupby("Clusters").mean(numeric_only=True)

print(clustered_summary)
df.dropna(subset=["Customer_ID"], inplace=True)


print(df.groupby("Clusters")["Education_Level"].value_counts())

print(df.groupby("Clusters")["Occupation"].value_counts())

print(df.groupby("Clusters")["Policy_Type"].value_counts())

df.to_csv("data/customer_segmented_data.csv", index=False)

print("Segmented dataset saved successfully!")


cluster_count = df["Clusters"].value_counts()

cluster_count.plot(kind="bar",figsize=(8,5), color = "blue")

plt.title("Cluster Distribution")
plt.xlabel("Clusters")
plt.ylabel("No of Customers")
plt.grid(True)
plt.savefig("images/Cluster_Distribution.png")
plt.show()


#PCA Visualization (Recommended)

#Since your dataset has many features (around 19), you can't directly plot the clusters in 2D.

#We use PCA (Principal Component Analysis) to reduce the data to 2 dimensions for visualization.


pca= PCA(n_components=2)
pca_data= pca.fit_transform(scaled_data)

# Now create the scatter plot:

plt.figure(figsize=(8,6))

plt.scatter(
    pca_data[:,0],
    pca_data[:,1],
    c=df["Clusters"],
    cmap="viridis"
)

plt.title("Customer Segments")
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")

plt.colorbar(label="Cluster")

plt.savefig("images/customer_segments.png")

plt.show()


