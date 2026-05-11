# Stored Procedure: `Sp_Check_GiaTriLechCacTruongTrenHopDong`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-02-21 14:01:44.490000
- **Ngày sửa cuối**: 2017-03-11 09:41:50.637000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayBatDau` | `nvarchar(100)` | No |
| `@NgayKetThuc` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
--Sp_Check_GiaTriLechCacTruongTrenHopDong '',''
CREATE PROCEDURE [dbo].[Sp_Check_GiaTriLechCacTruongTrenHopDong]
    @NgayBatDau NVARCHAR(50) ,
    @NgayKetThuc NVARCHAR(50)
AS
    BEGIN

        DECLARE @LastSynTime DATETIME
        DECLARE @MaxTimeSynInHD DATETIME
        DECLARE @FromDate DATETIME
        SET @MaxTimeSynInHD = ( SELECT  MAX(LastModifiedAt)
                                FROM    dbo.HopDong
                              )

        IF @NgayKetThuc = ''
            SET @LastSynTime = GETDATE()
        ELSE
            SET @LastSynTime = @NgayKetThuc
        IF @NgayBatDau = ''
            SET @FromDate = DATEADD(DD, -2, @LastSynTime)
        ELSE
            SET @FromDate = @NgayBatDau
      
		
		
        CREATE TABLE #HopDongTemp
            (
              id INT ,
              khachhang_id INT ,
              mahd_id INT ,
              so INT ,
              thang INT ,
              nam INT ,
              ngayky DATETIME ,
              ngaydanhsohd DATETIME ,
              loaikhachhang_id INT ,
              hinhthuckhachhang_id INT ,
              nhanvien_id INT ,
              phong_id INT ,
              bophan_id INT ,
              nhom_id INT ,
              diadiemlv_id INT ,
              nhanhd NVARCHAR(1000) ,
              TenNhanHopDong NVARCHAR(1000) ,
              idNhanHopDong INT ,
              giatrihd FLOAT ,
              trangthai INT ,
              LastModifyAt DATETIME
            )

        DECLARE @SQL NVARCHAR(MAX) 
		
        SET @SQL = 'select * FROM hdcn_hd where CONVERT(LastModifyAt,DATE) between '''''
            + CONVERT(NVARCHAR(20), @FromDate, 120) + ''''' AND '''''
            + CONVERT(NVARCHAR(20), @LastSynTime, 120) + '''''
	and trangthai <>0
	;'
        SET @SQL = '
					SELECT id	,
					khachhang_id	,
					mahd_id	,
					so	,
					thang	,
					nam	,
					ngayky	,
					ngaydanhsohd	,
					loaikhachhang_id	,
					hinhthuckhachhang_id	,
					nhanvien_id	,
					phong_id	,
					bophan_id	,
					nhom_id	,
					diadiemlv_id	,
					ISNULL(nhanhd,'''') nhanhd,
					ISNULL(TenNhanHopDong,'''') TenNhanHopDong	,
					ISNULL(idNhanHopDong,0)DmNhanHangGocREF	,
					giatrihd	,
					trangthai,
					LastModifyAt	 
					FROM OPENQUERY(MySQL,''' + @SQL + ''') 
					'
        PRINT @SQL
        INSERT  #HopDongTemp
                EXECUTE ( @SQL
                       )
		DECLARE @TotalRows INT
		DECLARE @x INT
		DECLARE @ColumnSQL NVARCHAR(500)
		DECLARE @ColumnMySQL NVARCHAR(500)
		DECLARE @DoiTuong NVARCHAR(500)
		SET @TotalRows  = (SELECT Max(STT) FROM ColumnCheckValue WHERE DoiTuong=N'Hợp đồng')
		SET @x=2
		WHILE @x<=@TotalRows
		BEGIN
			SELECT @ColumnSQL = ColumnSQL FROM ColumnCheckValue A WHERE STT=@x AND DoiTuong=N'Hợp đồng'
			SELECT @ColumnMySQL = ColumnMySQL FROM ColumnCheckValue A WHERE STT=@x AND DoiTuong=N'Hợp đồng'
			SELECT @DoiTuong = DoiTuong FROM ColumnCheckValue WHERE STT=@x AND DoiTuong=N'Hợp đồng'
			SET @SQL = '
			SELECT  '''+@ColumnSQL+''' [Column], 
					N'''+@DoiTuong+''' DoiTuong, 
					B.HopDongID,
					B.'+@ColumnSQL+' DulieuSQL,
					A.'+@ColumnMySQL+' DulieuMySQL,
					''Lech du lieu'' LoaiVanDe,
					'''+CONVERT(NVARCHAR(100),GETDATE(),113)+''' ThoiGianLog,
					0 TrangThaiXuLy,
					14 IDLoai
			FROM    #HopDongTemp A FULL JOIN
			(
			SELECT  *
			FROM    dbo.HopDong
			WHERE   CONVERT(DATE,LastModifiedAt) BETWEEN  '''+CONVERT(NVARCHAR(100),@FromDate,113)+''' AND '''+CONVERT(NVARCHAR(100), @LastSynTime ,113)+'''
			) B ON A.id=B.HopDongID
			WHERE 1=1 
			AND B.'+@ColumnSQL+'<> A.'+@ColumnMySQL+'
			AND CONVERT(DATE,a.LastModifyAt) <='''+CONVERT(NVARCHAR(50),@MaxTimeSynInHD,113)+''''
			INSERT INTO CheckThongTinDauVao
			EXECUTE(@SQL)
			SET @x = @x+1
		END
		
    END
	--Sp_Check_GiaTriLechCacTruongTrenHopDong '',''

```
