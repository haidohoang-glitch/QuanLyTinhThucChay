# Stored Procedure: `sp_KSTC_CheckSynData_CreatorContent`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2021-12-30 11:21:06.423000
- **Ngày sửa cuối**: 2021-12-30 13:50:00.297000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[sp_KSTC_CheckSynData_CreatorContent]

	-- Add the parameters for the stored procedure here

AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- 1. Check bảng Operating_Result
	SELECT N'CreatorContent_Operating_Result'as CheckSynData,  A.*,        B.* FROM (

        SELECT *-- Id,D_Products_Id,Operating_Order_Id,AdAccount_Name,AdAccount_Id,IsDeleted
        FROM [asdag2].ADS.dbo.Operating_Result                                                                                                          
        WHERE 1=1        
        --AND IsDeleted = 0
        and convert(date,creationTime) <= dateadd(d,-1,getdate())
        --AND LastModificationTime <= '2020-08-28 16:19:43.2142239'
)A                                                                                                                
FULL OUTER JOIN                                                                                                                                                                                                                        
(                                                                                                                
        SELECT *--Id,[Product Id],Operating_Order_Id,AdAccount_Name,AdAccount_Id,IsDeleted
        FROM ADS_Operating_Result                
        WHERE 1=1        --AND IsDeleted = 0                                                                                                                                                                                                                                                                                                                        
        and convert(date,creationTime) <= dateadd(d,-1,getdate())
)B        
ON A.Id = B.Id                                                                                                                
WHERE 1=1 
AND NOT (A.IsDeleted = 1 and B.IsDeleted = 1)
AND(
A.Id IS NULL OR B.Id IS NULL
--OR        A.[Product Id]        <>        B.[Product Id]        OR A.[Product Id] IS NULL OR B.[Product Id] IS NULL
--OR        A.[Product Name]        <>        B.[Product Name]        OR A.[Product Name] IS NULL OR B.[Product Name] IS NULL
OR        A.Operating_Order_Id        <>        B.Operating_Order_Id        OR A.Operating_Order_Id IS NULL OR B.Operating_Order_Id IS NULL
OR        isnull(A.AdAccount_Name,0)        <>        isnull(B.AdAccount_Name,0)--        OR A.AdAccount_Name IS NULL OR B.AdAccount_Name IS NULL
OR        A.AdAccount_Id        <>        B.AdAccount_Id        OR A.AdAccount_Id IS NULL OR B.AdAccount_Id IS NULL
OR        A.IsDeleted        <>        B.IsDeleted        OR A.IsDeleted IS NULL OR B.IsDeleted IS NULL
OR        A.Campaign_Id        <>        B.Campaign_Id        OR A.Campaign_Id IS NULL OR B.Campaign_Id IS NULL
OR        A.Campaign_Name        <>        B.Campaign_Name        OR A.Campaign_Name IS NULL OR B.Campaign_Name IS NULL
OR isnull(round(A.Exchange_Rate,0),0)        <>        isnull(round(B.Exchange_Rate,0),0)--        OR A.Exchange_Rate IS NULL OR B.Exchange_Rate IS NULL
OR        A.Start_Date        <>        B.Start_Date        OR A.Start_Date IS NULL OR B.Start_Date IS NULL
OR        isnull(A.Result_Type,0)        <>        isnull(B.Result_Type,0)--        OR A.Result_Type IS NULL OR B.Result_Type IS NULL
OR        isnull(A.Result,0)        <>        isnull(B.Result,0)--        OR A.Result IS NULL OR B.Result IS NULL
OR        A.Reach        <>        B.Reach        OR A.Reach IS NULL OR B.Reach IS NULL
OR        A.Impression        <>        B.Impression        OR A.Impression IS NULL OR B.Impression IS NULL
OR        A.Amoun_Spent        <>        B.Amoun_Spent        OR A.Amoun_Spent IS NULL OR B.Amoun_Spent IS NULL
OR        A.Frequency        <>        B.Frequency        OR A.Frequency IS NULL OR B.Frequency IS NULL
OR        isnull(A.CPC,0)        <>        isnull(B.CPC,0)--        OR A.CPC IS NULL OR B.CPC IS NULL
OR        A.CTR        <>        B.CTR        OR A.CTR IS NULL OR B.CTR IS NULL
OR        isnull(round(A.Cost_Per_Result,4),0)        <>        isnull(B.Cost_Per_Result,0)--        OR A.Cost_Per_Result IS NULL OR B.Cost_Per_Result IS NULL
OR        A.Clicks        <>        B.Clicks        OR A.Clicks IS NULL OR B.Clicks IS NULL
OR        A.CPM        <>        B.CPM        OR A.CPM IS NULL OR B.CPM IS NULL
OR        isnull(A.Cost_Per_Thousand_People_Reached,0)        <>        isnull(B.Cost_Per_Thousand_People_Reached,0)--        OR A.Cost_Per_Thousand_People_Reached IS NULL OR B.Cost_Per_Thousand_People_Reached IS NULL
OR        isnull(A.Page_Likes,0)        <>        isnull(B.Page_Likes,0)--        OR A.Page_Likes IS NULL OR B.Page_Likes IS NULL
OR        isnull(A.Post_Engagement,0)        <>        isnull(B.Post_Engagement,0)--        OR A.Post_Engagement IS NULL OR B.Post_Engagement IS NULL
OR        isnull(round(A.Cost_Per_Page_Like,4),0)        <>        isnull(B.Cost_Per_Page_Like,0)--        OR A.Cost_Per_Page_Like IS NULL OR B.Cost_Per_Page_Like IS NULL
OR        isnull(round(A.Cost_Per_Post_Engagement,4),0)        <>        isnull(B.Cost_Per_Post_Engagement,0)--        OR A.Cost_Per_Post_Engagement IS NULL OR B.Cost_Per_Post_Engagement IS NULL
OR        isnull(A.Leads,0)        <>        isnull(B.Leads,0)--        OR A.Leads IS NULL OR B.Leads IS NULL
OR        isnull(A.Total_Money_VND,0)        <>        isnull(B.Total_Money_VND,0)--        OR A.Total_Money_VND IS NULL OR B.Total_Money_VND IS NULL
OR        isnull(A.Sell_Money_VND,0)        <>        isnull(B.Sell_Money_VND,0)--        OR A.Sell_Money_VND IS NULL OR B.Sell_Money_VND IS NULL
OR        isnull(A.[View],0)        <>        isnull(B.[View],0)--        OR A.[View] IS NULL OR B.[View] IS NULL
OR        isnull(A.Conversions,0)        <>        isnull(B.Conversions,0)--        OR A.Conversions IS NULL OR B.Conversions IS NULL
OR        isnull(A.CPV,0)        <>        isnull(B.CPV,0)--        OR A.CPV IS NULL OR B.CPV IS NULL
OR        A.CreationTime        <>        B.CreationTime        OR A.CreationTime IS NULL OR B.CreationTime IS NULL
--OR        A.Age        <>        B.Age        OR A.Age IS NULL OR B.Age IS NULL
--OR        A.Sex        <>        B.Sex        OR A.Sex IS NULL OR B.Sex IS NULL
--OR        A.Regions        <>        B.Regions        OR A.Regions IS NULL OR B.Regions IS NULL
)

order by A.LastModificationTime


----2. Check bảng Operating_Result_Map_Order

SELECT N'CreatorContent_Operating_Result_Map_Order' as CheckSynData, A.*,B.* FROM (
        SELECT *        
        FROM [asdag2].ADS.dbo.Operating_Result_Map_Order                                                                                                         
        WHERE 1=1        
        --AND IsDeleted = 0
        --AND CreationTime < '2020-08-28'
        --AND convert(date,LastModificationTime) <= '2020-09-28 16:19:43.2142239'
        --select max(LastModificationTime) from  [asdag].ADS.dbo.Operating_Result_Map_Order
        and convert(date,creationTime) <= dateadd(d,-1,getdate())

)A                                                                                                                
FULL OUTER JOIN                                                                                                                                                                                                                        
(                                                                                                                
        SELECT-- max(LastModificationTime)
        *                
        FROM ADS_Operating_Result_Map_Order                
        WHERE 1=1        --AND IsDeleted = 0                
        and convert(date,creationTime) <= dateadd(d,-1,getdate())
)B        
ON A.Id = B.Id                                                                                                                
WHERE 1=1  AND
not (A.IsDeleted= 1 and B.IsDeleted = 1)
AND(
A.Id IS NULL OR B.Id IS NULL
OR        A.Operating_Order_Id        <>        B.Operating_Order_Id        OR A.Operating_Order_Id IS NULL OR B.Operating_Order_Id IS NULL
OR        A.operating_Result_Id        <>        B.operating_Result_Id        OR A.operating_Result_Id IS NULL OR B.operating_Result_Id IS NULL
OR        isnull(A.Result,0)        <>        isnull(B.Result,0)        
OR        isnull(A.Sell_Money_VND,0)        <>        isnull(B.Sell_Money_VND,0)
OR        A.CreationTime        <>        B.CreationTime        OR A.CreationTime IS NULL OR B.CreationTime IS NULL
--OR        A.LastModificationTime        <>        B.LastModificationTime        
OR A.LastModificationTime IS NULL OR B.LastModificationTime IS NULL
OR        A.IsDeleted        <>        B.IsDeleted        OR A.IsDeleted IS NULL OR B.IsDeleted IS NULL
)
order by A.LastModificationTime 


----3. Check bảng Operating_Order

SELECT N'CreatorContent_Operating_Order' as CheckSynData, A.*,B.* FROM (
        SELECT ID, Code,Contract_Id,Contract_Number,Contract_Detail_Id,Product_Id,Money_Turnover,From_Date,To_Date,
        Campaign_Type,Status,CreationTime,LastModificationTime,IsDeleted
        FROM [asdag2].ADS.dbo.Operating_Order                                                                                                        
        WHERE 1=1--        and LastModificationTime is null
        AND IsDeleted = 0
        and Contract_detail_id <> 0
        --and CreationTime <'2020-09-25 09:40:00'
        --AND LastModificationTime <= '2020-08-28 16:19:43.2142239'
        --select top 1 * from [asdag].ADS.dbo.Operating_Order
)A                                                                                                                
FULL OUTER JOIN                                                                                                                                                                                                                        
(                                                                                                                
        SELECT ID, Code,Contract_Id,Contract_Number,Contract_Detail_Id,Product_Id,Money_Turnover,From_Date,To_Date,
        Campaign_Type,Status,CreationTime,LastModificationTime, IsDeleted                                        
        FROM ADS_Operating_Order ttr                
        WHERE 1=1        AND IsDeleted = 0                
        and Contract_detail_id <> 0
)B        
ON A.Id = B.Id                                                                                                                
WHERE 1=1 AND (
 --A.Id IS NULL OR B.Id IS NULL
        convert(nvarchar(50),A.Code)        <>        convert(nvarchar(50),B.Code)        OR A.Code IS NULL OR B.Code IS NULL
        OR        A.Contract_Id        <>        B.Contract_Id        OR A.Contract_Id IS NULL OR B.Contract_Id IS NULL
        OR        isnull(A.Contract_Number,'') <> isnull(B.Contract_Number,'')--        OR A.Contract_Number IS NULL OR B.Contract_Number IS NULL
        OR        A.Contract_Detail_Id        <>        B.Contract_Detail_Id        OR A.Contract_Detail_Id IS NULL OR B.Contract_Detail_Id IS NULL
        OR        A.Product_Id        <>        B.Product_Id        OR A.Product_Id IS NULL OR B.Product_Id IS NULL
        OR        A.Money_Turnover        <>        B.Money_Turnover        OR A.Money_Turnover IS NULL OR B.Money_Turnover IS NULL
        OR        A.Campaign_Type        <>        B.Campaign_Type        OR A.Campaign_Type IS NULL OR B.Campaign_Type IS NULL
        ----OR        A.Status        <>        B.Status        OR A.Status IS NULL OR B.Status IS NULL
        OR        A.CreationTime        <>        B.CreationTime        OR A.CreationTime IS NULL OR B.CreationTime IS NULL
        ----OR        A.LastModificationTime        <>        B.LastModificationTime        
        OR A.LastModificationTime IS NULL OR B.LastModificationTime IS NULL
        OR        A.IsDeleted        <>        B.IsDeleted        OR A.IsDeleted IS NULL OR B.IsDeleted IS NULL                                                                                                                
)
ORDER BY A.LastModificationTime, A.CreationTime



----4. Check syn Operating_Result_Quantity

SELECT N'CreatorContent_Operating_Result_Quantity' as CheckSynData, A.*,B.* FROM (

        SELECT Id, D_Products_Id,UnitPrice,TotalMoney,FromDate,ToDate,UserConfirm,DateConfirm,
        Status,CreatorUserId,CreationTime,Operating_Order_Id,Quantity,LastModificationTime,IsDeleted
        FROM [asdag2].ADS.dbo.Operating_Result_Quantity                                                                                        
        WHERE 1=1        
        AND IsDeleted = 0
        --AND CreationTime < '2020-08-28'
        --AND LastModificationTime <= '2020-08-28 16:19:43.2142239'
)A                                                                                                                
FULL OUTER JOIN                                                                                                                                                                                                                        
(                                                                                                                
        SELECT Id, D_Products_Id,UnitPrice,TotalMoney,FromDate,ToDate,UserConfirm,DateConfirm,
        Status,CreatorUserId,CreationTime,Operating_Order_Id,Quantity,LastModificationTime,IsDeleted                
        FROM ADS_Operating_Result_Quantity                
        WHERE 1=1        AND IsDeleted = 0                                                                                                                                                                                                                                                                                                                        
)B        
ON A.Id = B.Id                                                                                                                
WHERE 1=1 AND (
         A.Id IS NULL OR B.Id IS NULL
        OR        A.D_Products_Id        <>        B.D_Products_Id        OR A.D_Products_Id IS NULL OR B.D_Products_Id IS NULL
        OR        A.Operating_Order_Id        <>        B.Operating_Order_Id        OR A.Operating_Order_Id IS NULL OR B.Operating_Order_Id IS NULL
        OR        A.Quantity        <>        B.Quantity        OR A.Quantity IS NULL OR B.Quantity IS NULL
        OR        A.UnitPrice        <>        B.UnitPrice        OR A.UnitPrice IS NULL OR B.UnitPrice IS NULL
        OR        A.TotalMoney        <>        B.TotalMoney        OR A.TotalMoney IS NULL OR B.TotalMoney IS NULL
        OR        A.FromDate        <>        B.FromDate        OR A.FromDate IS NULL OR B.FromDate IS NULL
        OR        A.ToDate        <>        B.ToDate        OR A.ToDate IS NULL OR B.ToDate IS NULL
        OR        ISNULL(A.UserConfirm,0)        <>        ISNULL(B.UserConfirm,0)
        OR        ISNULL(A.DateConfirm,getdate())        <>        ISNULL(B.DateConfirm,getdate())
        OR        A.Status        <>        B.Status        OR A.Status IS NULL OR B.Status IS NULL
        ----OR        A.CreatorUserId        <>        B.CreatorUserId        OR A.CreatorUserId IS NULL OR B.CreatorUserId IS NULL
        OR        convert(date,A.CreationTime)        <>        convert(date,B.CreationTime)        OR A.CreationTime IS NULL OR B.CreationTime IS NULL
        ----OR        A.LastModificationTime        <>        B.LastModificationTime        
        OR A.LastModificationTime IS NULL OR B.LastModificationTime IS NULL
        OR        A.IsDeleted        <>        B.IsDeleted        OR A.IsDeleted IS NULL OR B.IsDeleted IS NULL                                                                                                
)
ORDER BY A.LastModificationTime,B.LastModificationTime DESC

END

```
